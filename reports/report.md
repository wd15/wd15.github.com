---
layout: post
title: Technical Report -- 04.30.13
---

% Integrating Computational Tools to Support the Design of Advanced Materials
% Daniel Wheeler, Theiss Research
% 10.01.12 -- 04.30.13

<!-- To build this use: -->
<!--      $ pandoc report.md -o report.pdf --biblio refs.bib -->

## Introduction

Progress has been made in the following areas.

  * Integration of two open source level set codes with [FiPy].

  * Release of the extreme fill 1D code.

  * Implementation and testing of the extreme fill 2D code.

  * Publication of ``Formation mechanisms of self-organized core/shell
  and core/shell/corona microstructures in liquid droplets of
  immiscible alloys'' [@Shi20131229].

  * [FiPy] improvements,

  * Integration of [Sumatra] into the Python workflow.

  * Using Jekyll as a lab notebook.

## Integration of Two Open Source Level Set Tools with [FiPy]

Both [LSMLIB] and [Scikit-fmm] are now integrated into the Python
framework and can be used directly from within [FiPy]. The [FiPy]
examples and test suite can be launched with either of these tools
based on a command line flag. This work supports the current research
on extreme bottom-up fill and superfill at NIST. Historically, there
has been a distinct lack of open source alternatives for the level set
method. This work hopes to address this be providing two options as
well as the possibility to easily pose general PDEs in conjunction
with level set equations to track interfaces in [FiPy].

The work unifies the [FiPy], [LSMLIB] and [Scikit-fmm] test suites
(using Doctest) so that each tool has an automated test suite for a
good number of identical test problems. This process uncovered
fundamental issues with each package. These issues have now been fixed
and patched back to the main source repositories.

The changes to [LSMLIB] included creating a Python interface, building
an automated test suite and enabling a number of level set features
required for the superfill examples. The major changes to the code
included:
 
 - [`08f1434379`](https://github.com/ktchu/LSMLIB/commit/08f1434379)`: Reconciling LSMLIB and Scikit-fmm tests …`
 - [`7286f8fa6f`](https://github.com/ktchu/LSMLIB/commit/7286f8fa6f)`: Changing python interface to more closely match Scikit-fmm.`
 - [`92e60b8662`](https://github.com/ktchu/LSMLIB/commit/92e60b8662)`: Cleaning up documentation …`
 - [`0702572c67`](https://github.com/ktchu/LSMLIB/commit/0702572c67)`: Update to enable 3D.`
 - [`0ef83e28ba`](https://github.com/ktchu/LSMLIB/commit/0ef83e28ba)`: Adding sphinx documentation infrastructure …`
 - [`e7c656c22c`](https://github.com/ktchu/LSMLIB/commit/e7c656c22c)`: Adding test cases from FiPy …`
 - [`378a1e126e`](https://github.com/ktchu/LSMLIB/commit/378a1e126e)`: Reorganizing file and directory structure …`
 - [`69b42875e5`](https://github.com/ktchu/LSMLIB/commit/69b42875e5)`: Making the Eikonal equation work. …`
 - [`41ec69778b`](https://github.com/ktchu/LSMLIB/commit/41ec69778b)`: Introducing a sensible naming scheme and making examples work …`
 - [`7d14c6cc25`](https://github.com/ktchu/LSMLIB/commit/7d14c6cc25)`: Calculation of the distance function with a fast marching method now …`
 - [`69afa1c6d1`](https://github.com/ktchu/LSMLIB/commit/69afa1c6d1)`: Putting pylsmlib under lsmlib. …`

The changes to [Scikit-fmm] included fixing the broken extension
velocity components, implementing second-order schemes, updating the
documentation and developing an automated test suite. The major
changes to the code included:
    
 - [`b73f384165`](https://github.com/scikit-fmm/scikit-fmm/commit/b73f384165)`: Applying a modified version of the second order patch. …`
 - [`5b793dfc7d`](https://github.com/scikit-fmm/scikit-fmm/commit/5b793dfc7d)`: Merge branch 'fipy-testing' into fipy`
 - [`4225219f61`](https://github.com/scikit-fmm/scikit-fmm/commit/4225219f61)`: Refactoring the tests to use Doctest. …`
 - [`ecd625a7ca`](https://github.com/scikit-fmm/scikit-fmm/commit/ecd625a7ca)`: Merge branch 'fipy-extension-velocities'`
 - [`fed12a02ef`](https://github.com/scikit-fmm/scikit-fmm/commit/fed12a02ef)`: Adding an 'ext_mask' argument for compatibility with FiPy. …`
 - [`8a167a5533`](https://github.com/scikit-fmm/scikit-fmm/commit/8a167a5533)`: Fix for issues with extension velocities. …`

## Release of the Extreme Fill 1D Code

To support the recent release of the 1D extreme fill paper
[@citeulike:12297802] the 1D code used to generate the results and
figures in the paper has recently been released. The code base
includes documentation, a test suite and a straight forward interface
to generate the exact figures in the paper. The code is hosted at
[Github](http://wd15.github.io/extremefill/).

[Figure 1](#extremefill1D) shows ther ouput from running the default
simulation for 10 time steps, which is enough to reach steady
state.

~~~~~~{.python}
import extremefill
extremefill.run(totalSteps=10)
~~~~~~

[extremefill1D]: kPlus10-small.png

![The negative x values represents the trench domain while the positive values represent the electrolyte domain. The red, blue, green and cyan curves represent normalized values for the cupric concentration, adsorbed suppressor, suppressor concentration and potential, respectively.][extremefill1D]

## Implementation of the Extreme Fill 2D Code

The extreme fill 1D model is currently being extended to 2D. The 1D
model uses transient terms for all the equations, however, the
electrode/electrolyte interface is held in a stationary position. This
idealized system explains the most puzzling aspect of extreme fill,
the initial formation of the "on" and "off" states of deposition (see
[Figure 2](#efexp)). While the 1D model captures qualitative aspects
of extreme fill, it is not particularly accurate for making fill/fail
predictions. The 2D extreme fill model aims to improve the accuracy by
using the level set method to model the moving interface in similar
way to the
[old 2D superfill models](http://www.ctcms.nist.gov/fipy/examples/levelSet/electroChem/README.html),
but now uses the
[new level set implementation](http://matforge.org/fipy/changeset/47184e1bf40e/fipy)
recently introduced into [FiPy][FiPy]. Figure 3 shows results from the
2D model. The extreme fill 2D model is hosted at
[Github](https://github.com/wd15/extremefill)

[efexp]: extremefill.png

![The image of deposition in a silicon via demonstrates the segregated nature extreme fill.][efexp]

[im]: im.png

![Fill contours for the base set of parameters.][im]

The code has a built in test suite that uses the 1D model for a number
of the test cases.  Recent work has explored the convergence behavior
of the 2D model for a number of control parameters including CFL
number, grid spacing, non-linear tolerance and linear
tolerance. Loosely edited raw data and images from this work are
embedded in an
[IPython notebook](https://github.com/wd15/extremefill-data/blob/master/convergence.ipynb),
which is presently being formatted for a blog post.

## Publication of ``Formation mechanisms of self-organized ...''

Computational support was provided to Rongpei Shi at Ohio State
University to develop models that were used in the publication on
core/shell microstructures [@Shi20131229]. The work used [FiPy] and
the [reactive wetting][reactivewetting] model to help understand the
anomaly of parasitic currents.  Simulations were carried out using the
[reactive wetting][reactivewetting] model to understand the magnitude
of the parasitic currents with multiple solid particles in a liquid
matrix as occurs in core/shell systems. The work guided the use of an
existing model at Ohio State for the core/shell system that suffered
from the anomaly of parasitic currents.

## FiPy Improvements

The main improvements to FiPy that Daniel Wheeler has actively
participated in include switching from Subversion to Git and
refactoring the level set module. Daniel Wheeler has
[written 55 emails][fipylist] on the FiPy mailing list and he has
contributed to closing the following tickets:

 * [`ticket 383`](http://matforge.org/fipy/ticket/383)`: move FiPy to
   distributed version control.`. FiPy has been switched from
   Suberversion to Git.

 * [`ticket 513`](http://matforge.org/fipy/ticket/513)`: convection
   problem with cylindrical grid`. Fixed issue with the cylindrical
   grids.
   
 * [`ticket 490`](http://matforge.org/fipy/ticket/490)`: Parallel bug
   in non-uniform grids and conflicting mesh class and factory
   function names`. Cleaned up naming schemes for the grid classes.

 * [`ticket 564`](http://matforge.org/fipy/ticket/564)`: Van Leer
   Convection`. Fixed a problem with the Van Leer Convection Term and
   included more limiter functions.
 
 * [`ticket 491`](http://matforge.org/fipy/ticket/491)`: Rename
   communicator instances`. The communicator instances were renamed to
   more sensible names and some communicator uses were cleaned up.
   
 * [`ticket 432`](http://matforge.org/fipy/ticket/432)`: LSMLIB
   Refactor`. See the
   [first section](#integration-of-two-open-source-level-set-tools-with-fipy).


## Integration of [Sumatra] into the Python Workflow

[Sumatra] is a lightweight system for recording the history and
provenance data for numerical simulations. It works particularly well
for scientists that are in the intermediate stage between developing a
code base and using that code base for active research. The
integration of Sumatra into the Python workflow has required the
following improvements to Sumatra:

 * To address concurrency issues for batch simulations lock files have
   been implemented for SQLite (see
   [Github](https://github.com/wd15/sumatra/blob/working/src/smtdecorator.py)).
   
 * As an alternative to SQLite changes have been make to Sumatra to
   allow PostgreSQL as the back end database (see
   [blog post](http://wd15.github.io/2013/04/08/configuring-sumatra-for-postgres/)).

 * Added URL tagging functionality to give permanent URLs for
   searches.
 
 * Added a customized markdown and HTML table based on queries. This
   enables the static display of records in blog posts and in the
   IPython notebook.
   
 * Created a Sumatra decorator class that deals with parameters as
   command line arguments.

Daniel Wheeler has contributed to
[7 threads](sumatralist)
on the Sumatra mailing list.

## Using Jekyll as a Lab Notebook

A [new lab notebook](http://wd15.github.io) has been started at Github
using the [Jekyll blogging tool](http://jekyllbootstrap.com/) to
replace the [old Trac blog][tracblog]. The main benefit of the
[old Trac blog][tracblog] was the close integration with the
Subversion repository, which is no longer used. The overriding benefit
of using Jekyll is having the posts stored as plain markup in a local
Git repository independently from either the blogging tool or the blog
design. Also, using Jekyll presents a very low barrier to switching
between blogging tools in contrast to Trac which has a considerable
overhead due to the difficulties extracting the data from the database
in a suitable format. There is also the added benefit of testing
locally before publishing.

A secondary benefit is the possibility of including IPython notebooks
as blog posts. Using a
[set of scripts](https://github.com/wd15/wd15.github.com/blob/a8681be209f44be20eead2de2e338beb128ee924/ipynb2jekyll),
the notebook is first rendered as markdown and then a second script
creates a post and cleans up some formatting issues including image
locations and maths rendering. This process is now entirely automated.

## References 

[FiPy]: http://www.ctcms.nist.gov/fipy/
[Sumatra]: http://neuralensemble.org/sumatra/
[LSMLIB]: http://ktchu.serendipityresearch.org/software/lsmlib/index.html
[Scikit-fmm]: https://github.com/scikit-fmm/
[reactivewetting]: http://www.ctcms.nist.gov/fipy/examples/reactiveWetting/generated/examples.reactiveWetting.liquidVapor1D.html#module-examples.reactiveWetting.liquidVapor1D)
[tracblog]: http://matforge.org/wd15/blog
[fipylist]: http://search.gmane.org/?query=&author=daniel.wheeler2%40gmail.com&group=gmane.comp.python.fipy&sort=date&DEFAULTOP=and&[=1&TOPDOC=50&xFILTERS=Gcomp.python.fipy-Adaniel.wheeler2%40gmail.com---A
[sumatralist]: https://groups.google.com/forum/?fromgroups=#!topicsearchin/sumatra-users/authorname:%22Daniel$20Wheeler%22
