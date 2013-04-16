---
layout: post
title: "convergence"
description: ""
category: 
tags: []
---
{% include JB/setup %}
# Extreme Fill 2D

The 2D version of the extreme fill seems to work as of acbffe7419dcc0101fcbe and all the tests pass.

## Test convergence

Sweep through the following parameters.

  * CFL
  * grid spacing
  * sweep tolerance
  * linear solver tolerance

To test convergence use $$\|\phi - \phi_0\|$$ where $$\phi_0$$ is the most refined simulation.

## Investigating CFL convergence

Simulations were run with CFL values of 0.01, 0.02, 0.04, 0.08, 0.16, 0.32 and 0.64. The following are the Sumatra records of the simulations.

<div class="highlight"><pre><span class="kn">from</span> <span class="nn">IPython.core.display</span> <span class="kn">import</span> <span class="n">Image</span>

<span class="n">Image</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s">&#39;cfl_records.png&#39;</span><span class="p">,</span> <span class="n">embed</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
</pre></div>


<pre>
    <IPython.core.display.Image at 0x44ccad0>
</pre>


<div class="highlight"><pre><span class="kn">from</span> <span class="nn">viewer</span> <span class="kn">import</span> <span class="n">Records</span>
<span class="kn">from</span> <span class="nn">viewer</span> <span class="kn">import</span> <span class="n">ContourViewer</span>
<span class="n">records</span> <span class="o">=</span> <span class="n">Records</span><span class="p">()</span><span class="o">.</span><span class="n">by_tag</span><span class="p">(</span><span class="s">&#39;CFL&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">by_tag</span><span class="p">(</span><span class="s">&#39;production&#39;</span><span class="p">)</span>
<span class="n">baseRecord</span> <span class="o">=</span> <span class="n">records</span><span class="o">.</span><span class="n">by_parameter</span><span class="p">(</span><span class="s">&#39;CFL&#39;</span><span class="p">,</span> <span class="mf">0.01</span><span class="p">)</span>
<span class="k">for</span> <span class="n">CFL</span> <span class="ow">in</span> <span class="p">(</span><span class="mf">0.02</span><span class="p">,</span> <span class="mf">0.04</span><span class="p">,</span> <span class="mf">0.08</span><span class="p">,</span> <span class="mf">0.16</span><span class="p">,</span> <span class="mf">0.32</span><span class="p">,</span> <span class="mf">0.64</span><span class="p">):</span>
    <span class="n">otherRecord</span> <span class="o">=</span> <span class="n">records</span><span class="o">.</span><span class="n">by_parameter</span><span class="p">(</span><span class="s">&#39;CFL&#39;</span><span class="p">,</span> <span class="n">CFL</span><span class="p">)</span>
    <span class="n">v</span> <span class="o">=</span> <span class="n">ContourViewer</span><span class="p">(</span><span class="n">baseRecord</span><span class="p">,</span> <span class="n">otherRecord</span><span class="p">)</span>
    <span class="n">v</span><span class="o">.</span><span class="n">plot</span><span class="p">()</span>
    
</pre></div>


    datafile ./Data/e07c8a307a1e/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_00.png)

    datafile ./Data/678975cf7009/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_01.png)

    datafile ./Data/a9431ee7da68/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_02.png)

    datafile ./Data/9f933d3ae816/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_03.png)

    datafile ./Data/36f7e8fa0702/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_04.png)

    datafile ./Data/a1e3ead836eb/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_05.png)


The following code snippets are from previous attempts at obtaining covergence assessments.

After assessing the images above, it is fairly clear that the agreement is adequate up to CFL=0.16, so CFL=0.1 will probably be good enough going forward. 

## Investigating Nx Convergence

Look at Nx values of 150, 300, 600, 1200 to start with.

<div class="highlight"><pre><span class="kn">from</span> <span class="nn">IPython.core.display</span> <span class="kn">import</span> <span class="n">Image</span>

<span class="n">Image</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s">&#39;nx_records.png&#39;</span><span class="p">,</span> <span class="n">embed</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
</pre></div>


<pre>
    <IPython.core.display.Image at 0x4ff1e10>
</pre>


<div class="highlight"><pre><span class="kn">from</span> <span class="nn">viewer</span> <span class="kn">import</span> <span class="n">Records</span>
<span class="kn">from</span> <span class="nn">viewer</span> <span class="kn">import</span> <span class="n">ContourViewer</span>
<span class="n">records</span> <span class="o">=</span> <span class="n">Records</span><span class="p">()</span><span class="o">.</span><span class="n">by_tag</span><span class="p">(</span><span class="s">&#39;batch2&#39;</span><span class="p">)</span>
<span class="n">baseRecord</span> <span class="o">=</span> <span class="n">records</span><span class="o">.</span><span class="n">by_parameter</span><span class="p">(</span><span class="s">&#39;Nx&#39;</span><span class="p">,</span> <span class="mi">1200</span><span class="p">)</span>
<span class="k">for</span> <span class="n">Nx</span> <span class="ow">in</span> <span class="p">(</span><span class="mi">150</span><span class="p">,</span> <span class="mi">300</span><span class="p">,</span> <span class="mi">600</span><span class="p">):</span>
    <span class="n">otherRecord</span> <span class="o">=</span> <span class="n">records</span><span class="o">.</span><span class="n">by_parameter</span><span class="p">(</span><span class="s">&#39;Nx&#39;</span><span class="p">,</span> <span class="n">Nx</span><span class="p">)</span>
    <span class="n">v</span> <span class="o">=</span> <span class="n">ContourViewer</span><span class="p">(</span><span class="n">baseRecord</span><span class="p">,</span> <span class="n">otherRecord</span><span class="p">,</span> <span class="n">colors</span><span class="o">=</span><span class="p">(</span><span class="s">&#39;r&#39;</span><span class="p">,))</span>
    <span class="n">v</span><span class="o">.</span><span class="n">plot</span><span class="p">()</span>
</pre></div>


    datafile ./Data/85626d5b2715/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_06.png)

    datafile ./Data/e66ca6267686/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_07.png)

    datafile ./Data/4282f5340892/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_08.png)



    Tue Mar 26 16:44:36 EDT 2013

Simulations for Nx=2400 and Nx=4800 have been launched for both inline (1675883 and 1675884) and non-inline. Some investigation demonstrated that inlining shaves of about 25% of the run time.

## Profiling

Profiling shows that the amout of time spent in the solver scales badly as the size of the grid is increased.


<div class="highlight"><pre><span class="c">## [Nx, total_time, time_in_solver, number_of_solvers]</span>
<span class="n">prof_results</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([[</span><span class="mi">150</span><span class="p">,</span> <span class="mf">4068.</span><span class="p">,</span> <span class="mf">300.</span><span class="p">,</span> <span class="mi">44</span><span class="p">],</span> <span class="p">[</span><span class="mi">300</span><span class="p">,</span> <span class="mf">9812.</span><span class="p">,</span> <span class="mf">2453.</span><span class="p">,</span> <span class="mi">44</span><span class="p">],</span> <span class="p">[</span><span class="mi">600</span><span class="p">,</span> <span class="mi">43866</span><span class="p">,</span> <span class="mi">20662</span><span class="p">,</span> <span class="mi">44</span><span class="p">],</span> <span class="p">[</span><span class="mi">1200</span><span class="p">,</span> <span class="mi">274268</span><span class="p">,</span> <span class="mi">191214</span><span class="p">,</span> <span class="mi">44</span><span class="p">]])</span>

<span class="n">N</span> <span class="o">=</span> <span class="n">prof_results</span><span class="p">[:,</span><span class="mi">0</span><span class="p">]</span><span class="o">**</span><span class="mi">2</span>
<span class="n">pl</span><span class="o">.</span><span class="n">loglog</span><span class="p">(</span><span class="n">N</span><span class="p">,</span> <span class="n">prof_results</span><span class="p">[:,</span><span class="mi">1</span><span class="p">],</span> <span class="s">&#39;k&#39;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">r&quot;total&quot;</span><span class="p">)</span>
<span class="n">pl</span><span class="o">.</span><span class="n">loglog</span><span class="p">(</span><span class="n">N</span><span class="p">,</span> <span class="n">prof_results</span><span class="p">[:,</span><span class="mi">2</span><span class="p">],</span> <span class="s">&#39;r&#39;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">r&quot;solver&quot;</span><span class="p">)</span>
<span class="n">pl</span><span class="o">.</span><span class="n">loglog</span><span class="p">(</span><span class="n">N</span><span class="p">,</span> <span class="mf">1e-2</span> <span class="o">*</span> <span class="n">N</span><span class="p">,</span> <span class="s">&#39;g--&#39;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">r&quot;$N$&quot;</span><span class="p">)</span>
<span class="n">pl</span><span class="o">.</span><span class="n">loglog</span><span class="p">(</span><span class="n">N</span><span class="p">,</span> <span class="mf">1e-6</span> <span class="o">*</span> <span class="n">N</span><span class="o">**</span><span class="mi">2</span><span class="p">,</span> <span class="s">&#39;b--&#39;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">r&quot;$N^2$&quot;</span><span class="p">)</span>
<span class="n">pl</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span>
<span class="n">pl</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>



![]({{ site.imageurl }}/convergence_files/convergence_fig_09.png)


## Sweeps

<div class="highlight"><pre><span class="kn">from</span> <span class="nn">IPython.core.display</span> <span class="kn">import</span> <span class="n">Image</span>

<span class="n">Image</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s">&#39;sweep_records.png&#39;</span><span class="p">,</span> <span class="n">embed</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
</pre></div>


<pre>
    <IPython.core.display.Image at 0x3b67f90>
</pre>


<div class="highlight"><pre><span class="kn">from</span> <span class="nn">viewer</span> <span class="kn">import</span> <span class="n">Records</span>
<span class="kn">from</span> <span class="nn">viewer</span> <span class="kn">import</span> <span class="n">ContourViewer</span>
<span class="n">records</span> <span class="o">=</span> <span class="n">Records</span><span class="p">()</span><span class="o">.</span><span class="n">by_tag</span><span class="p">(</span><span class="s">&#39;serialnumber4&#39;</span><span class="p">)</span>
<span class="n">baseRecord</span> <span class="o">=</span> <span class="n">records</span><span class="o">.</span><span class="n">by_parameter</span><span class="p">(</span><span class="s">&#39;sweeps&#39;</span><span class="p">,</span> <span class="mi">32</span><span class="p">)</span>
<span class="k">for</span> <span class="n">sweeps</span> <span class="ow">in</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">16</span><span class="p">):</span>
    <span class="n">otherRecord</span> <span class="o">=</span> <span class="n">records</span><span class="o">.</span><span class="n">by_parameter</span><span class="p">(</span><span class="s">&#39;sweeps&#39;</span><span class="p">,</span> <span class="n">sweeps</span><span class="p">)</span>
    <span class="n">v</span> <span class="o">=</span> <span class="n">ContourViewer</span><span class="p">(</span><span class="n">baseRecord</span><span class="p">,</span> <span class="n">otherRecord</span><span class="p">,</span> <span class="n">colors</span><span class="o">=</span><span class="p">(</span><span class="s">&#39;r&#39;</span><span class="p">,))</span>
    <span class="n">v</span><span class="o">.</span><span class="n">plot</span><span class="p">()</span>
</pre></div>


    datafile ./Data/331ce2cd522c/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_10.png)

    datafile ./Data/528f07e88fae/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_11.png)

    datafile ./Data/e16fa2b84942/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_12.png)

    datafile ./Data/8307dc417ea0/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_13.png)

    datafile ./Data/7a17de0b7487/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_14.png)


## Solver Tolerance

<div class="highlight"><pre><span class="kn">from</span> <span class="nn">IPython.core.display</span> <span class="kn">import</span> <span class="n">Image</span>

<span class="n">Image</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s">&#39;solver_tol_records.png&#39;</span><span class="p">,</span> <span class="n">embed</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
</pre></div>


<pre>
    <IPython.core.display.Image at 0x501d450>
</pre>


<div class="highlight"><pre><span class="kn">from</span> <span class="nn">viewer</span> <span class="kn">import</span> <span class="n">Records</span>
<span class="kn">from</span> <span class="nn">viewer</span> <span class="kn">import</span> <span class="n">ContourViewer</span>
<span class="n">records</span> <span class="o">=</span> <span class="n">Records</span><span class="p">()</span><span class="o">.</span><span class="n">by_tag</span><span class="p">(</span><span class="s">&#39;serialnumber7&#39;</span><span class="p">)</span>
<span class="n">baseRecord</span> <span class="o">=</span> <span class="n">records</span><span class="o">.</span><span class="n">by_parameter</span><span class="p">(</span><span class="s">&#39;solver_tol&#39;</span><span class="p">,</span> <span class="mf">1e-7</span><span class="p">)</span>
<span class="k">for</span> <span class="n">solver_tol</span> <span class="ow">in</span> <span class="p">(</span><span class="mf">1e-1</span><span class="p">,</span> <span class="mf">1e-2</span><span class="p">,</span> <span class="mf">1e-3</span><span class="p">,</span> <span class="mf">1e-4</span><span class="p">,</span> <span class="mf">1e-5</span><span class="p">,</span> <span class="mf">1e-6</span><span class="p">):</span>
    <span class="n">otherRecord</span> <span class="o">=</span> <span class="n">records</span><span class="o">.</span><span class="n">by_parameter</span><span class="p">(</span><span class="s">&#39;solver_tol&#39;</span><span class="p">,</span> <span class="n">solver_tol</span><span class="p">)</span>
    <span class="n">v</span> <span class="o">=</span> <span class="n">ContourViewer</span><span class="p">(</span><span class="n">baseRecord</span><span class="p">,</span> <span class="n">otherRecord</span><span class="p">,</span> <span class="n">colors</span><span class="o">=</span><span class="p">(</span><span class="s">&#39;r&#39;</span><span class="p">,))</span>
    <span class="n">v</span><span class="o">.</span><span class="n">plot</span><span class="p">()</span>
</pre></div>


    datafile ./Data/2531d84308b4/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_15.png)

    datafile ./Data/5ad7bdc1a530/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_16.png)

    datafile ./Data/33b8c8063ac2/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_17.png)

    datafile ./Data/417bcf854132/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_18.png)

    datafile ./Data/9bc8c7395961/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_19.png)

    datafile ./Data/f59dfdbec834/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_20.png)


## New settings

Due to the last two batch simulations, the default parameters have been switched to

```python
sweeps = 4
solver_tol = 1e-6
CFL = 0.1```

Using these new parameters, simulations have been run with ```python Nx=150, 300, 600, 1200, 2400```. This is to see if run times are reduced with these new settings. It seems like the finer grids spend rather a lot of time doing loads of iterations near the end of the run after things have reached a steady state. As an expendient measure, just setting the ```python sweeps = 4``` gets around all the issues with the non-linear tolerance setting.


## Direct comparison with old parameter values

<div class="highlight"><pre><span class="kn">from</span> <span class="nn">viewer</span> <span class="kn">import</span> <span class="n">Records</span>
<span class="kn">from</span> <span class="nn">viewer</span> <span class="kn">import</span> <span class="n">ContourViewer</span>
<span class="n">records</span> <span class="o">=</span> <span class="n">Records</span><span class="p">()</span><span class="o">.</span><span class="n">by_tag</span><span class="p">(</span><span class="s">&#39;serialnumber8&#39;</span><span class="p">)</span>
<span class="n">baseRecords</span> <span class="o">=</span> <span class="n">Records</span><span class="p">()</span><span class="o">.</span><span class="n">by_tag</span><span class="p">(</span><span class="s">&#39;batch2&#39;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">Nx</span> <span class="ow">in</span> <span class="p">(</span><span class="mi">150</span><span class="p">,</span> <span class="mi">300</span><span class="p">,</span> <span class="mi">600</span><span class="p">):</span>
    <span class="n">baseRecord</span> <span class="o">=</span> <span class="n">baseRecords</span><span class="o">.</span><span class="n">by_parameter</span><span class="p">(</span><span class="s">&#39;Nx&#39;</span><span class="p">,</span> <span class="n">Nx</span><span class="p">)</span>
    <span class="n">otherRecord</span> <span class="o">=</span> <span class="n">records</span><span class="o">.</span><span class="n">by_parameter</span><span class="p">(</span><span class="s">&#39;Nx&#39;</span><span class="p">,</span> <span class="n">Nx</span><span class="p">)</span>
    <span class="n">v</span> <span class="o">=</span> <span class="n">ContourViewer</span><span class="p">(</span><span class="n">baseRecord</span><span class="p">,</span> <span class="n">otherRecord</span><span class="p">,</span> <span class="n">colors</span><span class="o">=</span><span class="p">(</span><span class="s">&#39;r&#39;</span><span class="p">,))</span>
    <span class="n">v</span><span class="o">.</span><span class="n">plot</span><span class="p">()</span>
</pre></div>


    datafile ./Data/3ee16bf59777/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_21.png)

    datafile ./Data/8cdf3a35f80f/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_22.png)

    datafile ./Data/d83505552902/data.h5


![]({{ site.imageurl }}/convergence_files/convergence_fig_23.png)


No change for 300 and 600, which is fine for present requirements. Following cell shows run times with new and old parameters.

<div class="highlight"><pre><span class="kn">from</span> <span class="nn">viewer</span> <span class="kn">import</span> <span class="n">Records</span>
<span class="kn">import</span> <span class="nn">pylab</span>
<span class="n">records</span> <span class="o">=</span> <span class="n">Records</span><span class="p">()</span><span class="o">.</span><span class="n">by_tag</span><span class="p">(</span><span class="s">&#39;serialnumber8&#39;</span><span class="p">)</span>
<span class="n">baseRecords</span> <span class="o">=</span> <span class="n">Records</span><span class="p">()</span><span class="o">.</span><span class="n">by_tag</span><span class="p">(</span><span class="s">&#39;batch2&#39;</span><span class="p">)</span>
<span class="n">tOld</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">tNew</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">Nxs</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">((</span><span class="mi">150</span><span class="p">,</span> <span class="mi">300</span><span class="p">,</span> <span class="mi">600</span><span class="p">))</span>
<span class="k">for</span> <span class="n">Nx</span> <span class="ow">in</span> <span class="n">Nxs</span><span class="p">:</span>
    <span class="n">tOld</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">baseRecords</span><span class="o">.</span><span class="n">by_parameter</span><span class="p">(</span><span class="s">&#39;Nx&#39;</span><span class="p">,</span> <span class="n">Nx</span><span class="p">)</span><span class="o">.</span><span class="n">records</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">duration</span><span class="p">)</span>
    <span class="n">tNew</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">records</span><span class="o">.</span><span class="n">by_parameter</span><span class="p">(</span><span class="s">&#39;Nx&#39;</span><span class="p">,</span> <span class="n">Nx</span><span class="p">)</span><span class="o">.</span><span class="n">records</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">duration</span><span class="p">)</span>
    
<span class="n">pylab</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">Nxs</span><span class="o">**</span><span class="mi">2</span><span class="p">,</span> <span class="n">tOld</span><span class="p">,</span> <span class="s">&#39;k&#39;</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">Nxs</span><span class="o">**</span><span class="mi">2</span><span class="p">,</span> <span class="n">tNew</span><span class="p">,</span> <span class="s">&#39;r&#39;</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
    
</pre></div>



![]({{ site.imageurl }}/convergence_files/convergence_fig_24.png)


As off ```Thu Mar 28 12:39:49 EDT 2013```, there are some ```python Nx=1200``` and ```python Nx=2400``` simulations running. The next step is to try and reproduce some of the results in the 1D paper. I'll try and reproduce the 2D color map in the paper.

