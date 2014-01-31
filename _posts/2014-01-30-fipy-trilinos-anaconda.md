---
layout: post
title: "FiPy, Trilinos and Anaconda"
category: posts
---

There was a recent question on the
[FiPy mailing list](http://article.gmane.org/gmane.comp.python.fipy/3372)
regarding running FiPy in parallel.

> My desired use case uses a nonuniform 3D grid (from
fipy.meshes.nonUniformGrid3D import NonUniformGrid3D).  Running this
in parallel, it takes about the same amount of time or longer.  If I
switch the same case to a uniform 3D grid (Grid3D), parallel execution
is faster than serial, as I expected (although not exactly optimal --
see attached plot).

I decided to look into this as I haven't been using FiPy in parallel
for awhile and haven't tested it for efficiency in even longer. I used
a [simple test case](https://gist.github.com/8717979.git), called
`kris.py`, to test FiPy in parallel. The test case is just a diffusion
problem on a 3D grid. It uses Gmsh to partition the grid sensibly as
the non-Gmsh grids in FiPy only use suboptimally sliced partitions. In
serial the test case ran without issues:

{% highlight bash %}
$ python kris.py
27900
0.185834884644
{% endhighlight %}

(with PySparse) and with Trilinos:

{% highlight bash %}
$ python kris.py --trilinos
27900
0.387823104858
{% endhighlight %}

The script, `kris.py`, uses `time` to measure the duration of one time
step. In general, it's better to use `timeit`, but a bit more fiddly
to set up. Anyway, Trilinos is quite a bit slower than PySparse, but I
know that the default solver selection along with the default
tolerance and number of iterations is not consistent between PySparse
and Trilinos. This accounts for some of the run time duration
discrepency, though not all.  At this stage I just want to check that
it's actually working in parallel so I tried running it with MPI:

{% highlight bash %}
$ mpirun -np 1 python kris.py --trilinos
[loki:18539] [[55252,1],0] routed:binomial: Connection to lifeline [[55252,0],0] lost
Traceback (most recent call last):
  File "kris.py", line 8, in <module>
    m = fp.GmshGrid3D(nx=N, ny=N, nz=N, dx=L / N, dy=L / N, dz=L / N)
  File "/home/wd15/git/fipy/fipy/meshes/gmshMesh.py", line 2239, in __init__
    Gmsh3D.__init__(self, arg, communicator=communicator, order=order)
  File "/home/wd15/git/fipy/fipy/meshes/gmshMesh.py", line 1937, in __init__
    background=background)
  File "/home/wd15/git/fipy/fipy/meshes/gmshMesh.py", line 151, in openMSHFile
    raise EnvironmentError("Gmsh version must be >= 2.0.")
EnvironmentError: Gmsh version must be >= 2.0.
{% endhighlight %}

The system version of Gmsh (installed with the package manager inp
Ubuntu) is 2.8.2 so FiPy's Python error message is clearly
inaccurate. I searched with the `routed:binomial` error message and
found
[a ticket that I'd filed ages ago and never really resolved](http://matforge.org/fipy/ticket/396#comment:7).
Looking at the ticket, it became clear that the real issue above is
that MPI is messing with Python's ability to communicate with a
subprocess. FiPy calls out to Gmsh as a subprocess to gather its
version number. This prompted me to reinstall Trilinos
again. Sometimes this has helped resolve issues in the past when I've
had an old version of Trilinos knocking around (maybe the system
libraries get out of sync with Trilinos).  Predictably, this resolved
the issue as far as Trilinos was concerned. However, `mpi4py`
generated exactly the the same subprocess communication issue (FiPy
requires `mpi4py` for parallel operation) and subsequent
reinstallation of `mpi4py` didn't help.

## Anaconda

I've been interested in switching from Virtualenv to Anaconda for some
time. I had a hunch that Anaconda might handle some of the issues with
library incompatibilities more seamlessly than using the system
installation along with Virtualenv. My understanding is that Anaconda
inherits none of the system installation (unlike Virtualenv).  First,
I made sure that FiPy worked in serial with Anaconda. This step
consisted of installing PySparse and maybe a few other packages (can't
remember exactly), but there were no issues getting FiPy set up in
serial.

Of course, to get FiPy working in parallel I needed to install
Trilinos. At first I installed Trilinos without realizing that
Anaconda comes with all the MPI compilers and libraries. I'd compiled
Trilinos against the system MPI libraries rather than Anaconda's, so
when running:

{% highlight bash %}
$ /usr/bin/mpirun -np 1 python kris.py --trilinos
{% endhighlight %}

it gave errors (which I unfortunately didn't record anywhere). The
Trilinos build recipe that was eventually used, after a few more
missteps, points at Anaconda's MPI:

{% highlight bash %}
EXTRA_ARGS=$@
TRILINOS_HOME=/home/wd15/pkg/trilinos-11.4.3-Source
CMAKE=cmake

${CMAKE} \
  -D CMAKE_BUILD_TYPE:STRING=RELEASE \
  -D Trilinos_ENABLE_PyTrilinos:BOOL=ON \
  -D BUILD_SHARED_LIBS:BOOL=ON \
  -D Trilinos_ENABLE_ALL_OPTIONAL_PACKAGES:BOOL=ON \
  -D TPL_ENABLE_MPI:BOOL=ON \
  -D MPI_BASE_DIR:PATH=${ANACONDA} \
  -D Trilinos_ENABLE_TESTS:BOOL=ON \
  -D DART_TESTING_TIMEOUT:STRING=600 \
  -D CMAKE_INSTALL_PREFIX:PATH=${ANACONDA} \
  -D PyTrilinos_INSTALL_PREFIX:PATH=${ANACONDA} \
  ${EXTRA_ARGS} \
  ${TRILINOS_HOME}
{% endhighlight %}

where the `ANACONDA` variable is just the base Anaconda
directory. After installing Trilinos correctly, the Gmsh subprocess
gave the following error with 2 processors:

{% highlight bash %}
$ mpirun -np 2 python kris.py --trilinos
*** Error in `gmsh': double free or corruption (out): 0x0000000003416ec0 ***
...
7f96602a0000 ... /usr/lib/openmpi/lib/openmpi/mca_osc_rdma.so
...
[loki:07916] *** End of error message ***
Traceback (most recent call last):
...
EOFError: No `MeshFormat' header found!
{% endhighlight %}

The Python error is just due to Gmsh falling over. The fact that the
error message is pointing at the system MPI is confusing and suggests
the system version of Gmsh is somehow compiled with MPI
support. However, `ENABLE_MPI=OFF` is the default setting for Gmsh
which seems inconsistent. Anyway, I didn't try to really resolve this
problem, but just updated the version of Gmsh without using the system
version. I downloaded the latest binary version of Gmsh and placed it
in Anaconda's `bin` directly and then everything seemed to work:

{% highlight bash %}
$ mpirun -np 1 python kris.py --trilinos
27900
0.372065067291
$ mpirun -np 2 python kris.py --trilinos
14973
14973
0.230810165405
0.230820894241
$ mpirun -np 4 python kris.py --trilinos
7971
7955
8106
7958
0.157829046249
0.157819032669
0.157863140106
0.157871007919
{% endhighlight %}

Of course, the above doesn't answer any of the original questions on
the mailing list, but at least I have a working version of FiPy in
parallel.


