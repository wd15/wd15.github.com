---
layout: post
title: "Extreme Fill 2D"
description: ""
category: 
tags: []
---

## Introduction

The extreme fill 1D model has been extended to 2D. Although, the 1D
model uses transient terms for all the equations, the
electrode/electrolyte interface is held in a stationary position. This
idealized system helps explain the most puzzling aspect of extreme fill,
the initial formation of the "on" and "off" states of deposition (see [previous blog post](http://wd15.github.io/2013/04/12/extreme-fill-explanation/). While the 1D model captures the most important qualitative aspect
of extreme fill, it is not particularly accurate for making fill/fail
predictions. The 2D extreme fill model aims to improve the accuracy by
using the level set method to model the moving interface in similar
way to the
[old 2D superfill models](http://www.ctcms.nist.gov/fipy/examples/levelSet/electroChem/README.html),
but now uses the
[new level set implementation](http://matforge.org/fipy/changeset/47184e1bf40e/fipy)
recently introduced into [FiPy](http://www.ctcms.nist.gov/fipy). The extreme fill 2D model is hosted at
[Github](https://github.com/wd15/extremefill).




### Note on IPython and Jekyll

This is a just a note on integrating the IPython notebook into the Jekyll blog. The [blog post by David Ketcheson](http://www.davidketcheson.info/2012/10/11/blogging_ipython_notebooks_with_jekyll.html) includes a script to automate the IPython to Jekyll transition. The script has been modified for my own needs (see [the script on Github](https://github.com/wd15/wd15.github.com/blob/master/ipynb2jekyll)). There are a number of issues that aren't yet ironed out such as embedding Sumatra markdown tables rather than HTML and including hover text with Sumatra labels for figures. 




### Demonstration

As a demonstration of the model, a movie has been made from the following [Sumatra](http://neuralensemble.org/sumatra/) record. This also demonstrates embedding a Sumatra table in IPython.

<div class="highlight"><pre><code class="python"><span class="kn">from</span> <span class="nn">smtext</span> <span class="kn">import</span> <span class="n">getSMTRecords</span><span class="p">,</span> <span class="n">CustomHTMLFormatter</span>
<span class="n">records</span> <span class="o">=</span> <span class="n">getSMTRecords</span><span class="p">(</span><span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;serialnumber18&#39;</span><span class="p">],</span><span class="n">parameters</span><span class="o">=</span><span class="p">{</span><span class="s">&#39;Nx&#39;</span> <span class="p">:</span> <span class="mi">600</span><span class="p">})</span>
<span class="n">CustomHTMLFormatter</span><span class="p">(</span><span class="n">records</span><span class="p">,</span> <span class="n">fields</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;label&#39;</span><span class="p">,</span> <span class="s">&#39;timestamp&#39;</span><span class="p">,</span> <span class="s">&#39;parameters&#39;</span><span class="p">,</span> <span class="s">&#39;repository&#39;</span><span class="p">,</span> <span class="s">&#39;version&#39;</span><span class="p">],</span> <span class="n">parameters</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;Nx&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">ipython_table</span><span class="p">()</span>
</code></pre></div>


<table style="border:2px solid black;border-collapse:collapse; font-size:10px;">
  <tr>
    <th style="border:2px solid black;background:#b5cfd2">Label</th>
    <th style="border:2px solid black;background:#b5cfd2">Timestamp</th>
    <th style="border:2px solid black;background:#b5cfd2">Parameters</th>
    <th style="border:2px solid black;background:#b5cfd2">Repository</th>
    <th style="border:2px solid black;background:#b5cfd2">Version    </th>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">58d17d49efd8</code></td>
    <td style="border:2px solid black;">2013-04-26 17:55</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">Nx: 600</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">a4e17af0c25a</code>    </td>
  </tr>
</table>
<br>

<p style="text-align: center;"><iframe width="480" height="360" src="http://www.youtube.com/embed/3I6KU9CymGo?rel=0" frameborder="0"> </iframe></p>



## Convergence

The following sections contain a rudimentary $$\chi$$ -by-eye convergence analysis. Further convergence testing may be done, but it is probably best to actually produce some useful results and revisit convergence when the model is closer to being finalized.




### CFL Number

The figures show convergence as the `CFL` decreases from `0.64` to `0.01`. The contours presented are for the time steps that have the closest elapsed times to the `times` argument (time step size is not uniform for these simulations). The red contour is for `CFL=0.01` (the base case).

<div class="highlight"><pre><code class="python"><span class="kn">from</span> <span class="nn">multiViewer</span> <span class="kn">import</span> <span class="n">MultiViewer</span>
<span class="kn">from</span> <span class="nn">smtext</span> <span class="kn">import</span> <span class="n">getSMTRecords</span><span class="p">,</span> <span class="n">CustomHTMLFormatter</span>

<span class="n">records</span> <span class="o">=</span> <span class="n">getSMTRecords</span><span class="p">(</span><span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;CFL&#39;</span><span class="p">,</span> <span class="s">&#39;production&#39;</span><span class="p">])</span>
<span class="n">records</span> <span class="o">=</span> <span class="p">[</span><span class="n">getSMTRecords</span><span class="p">(</span><span class="n">records</span><span class="o">=</span><span class="n">records</span><span class="p">,</span> <span class="n">parameters</span><span class="o">=</span><span class="p">{</span><span class="s">&#39;CFL&#39;</span> <span class="p">:</span> <span class="n">CFL</span><span class="p">})[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">CFL</span> <span class="ow">in</span> <span class="p">(</span><span class="mf">0.01</span><span class="p">,</span> <span class="mf">0.02</span><span class="p">,</span> <span class="mf">0.04</span><span class="p">,</span> <span class="mf">0.08</span><span class="p">,</span> <span class="mf">0.16</span><span class="p">,</span> <span class="mf">0.32</span><span class="p">,</span> <span class="mf">0.64</span><span class="p">)]</span>
<span class="n">title</span> <span class="o">=</span> <span class="p">[</span><span class="s">r&#39;CFL={0:1.2f}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">r</span><span class="o">.</span><span class="n">parameters</span><span class="p">[</span><span class="s">&#39;CFL&#39;</span><span class="p">])</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">records</span><span class="p">[</span><span class="mi">1</span><span class="p">:]]</span>
<span class="n">viewer</span> <span class="o">=</span> <span class="n">MultiViewer</span><span class="p">(</span><span class="n">records</span><span class="p">[</span><span class="mi">1</span><span class="p">:],</span> <span class="n">baseRecords</span><span class="o">=</span><span class="n">records</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">title</span><span class="o">=</span><span class="n">title</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">12</span><span class="p">,</span> <span class="mi">9</span><span class="p">))</span>
<span class="n">viewer</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">times</span><span class="o">=</span><span class="p">(</span><span class="mf">0.</span><span class="p">,</span> <span class="mf">1000.</span><span class="p">,</span> <span class="mf">2000.</span><span class="p">,</span> <span class="mf">3000.</span><span class="p">,</span> <span class="mf">4000.</span><span class="p">))</span>
<span class="n">CustomHTMLFormatter</span><span class="p">(</span><span class="n">records</span><span class="p">,</span> <span class="n">fields</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;label&#39;</span><span class="p">,</span> <span class="s">&#39;timestamp&#39;</span><span class="p">,</span> <span class="s">&#39;parameters&#39;</span><span class="p">,</span> <span class="s">&#39;repository&#39;</span><span class="p">,</span> <span class="s">&#39;version&#39;</span><span class="p">,</span> <span class="s">&#39;duration&#39;</span><span class="p">],</span> <span class="n">parameters</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;CFL&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">ipython_table</span><span class="p">()</span>
</code></pre></div>



![]({{ site.imageurl }}/extremefill2D_files/extremefill2D_fig_00.png)

<table style="border:2px solid black;border-collapse:collapse; font-size:10px;">
  <tr>
    <th style="border:2px solid black;background:#b5cfd2">Label</th>
    <th style="border:2px solid black;background:#b5cfd2">Timestamp</th>
    <th style="border:2px solid black;background:#b5cfd2">Parameters</th>
    <th style="border:2px solid black;background:#b5cfd2">Repository</th>
    <th style="border:2px solid black;background:#b5cfd2">Version</th>
    <th style="border:2px solid black;background:#b5cfd2">Duration    </th>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">76cc1cca1d89</code></td>
    <td style="border:2px solid black;">2013-02-22 13:40</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">CFL: 0.01</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">0e0334ae83ae</code></td>
    <td style="border:2px solid black;">6h 9m 0.42s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">e07c8a307a1e</code></td>
    <td style="border:2px solid black;">2013-02-22 13:40</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">CFL: 0.02</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">0e0334ae83ae</code></td>
    <td style="border:2px solid black;">3h 41m 14.56s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">678975cf7009</code></td>
    <td style="border:2px solid black;">2013-02-22 13:40</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">CFL: 0.04</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">0e0334ae83ae</code></td>
    <td style="border:2px solid black;">2h 19m 31.04s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">a9431ee7da68</code></td>
    <td style="border:2px solid black;">2013-02-21 16:32</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">CFL: 0.08</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">0592f3835b5c</code></td>
    <td style="border:2px solid black;">1h 18m 11.83s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">9f933d3ae816</code></td>
    <td style="border:2px solid black;">2013-02-21 16:32</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">CFL: 0.16</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">0592f3835b5c</code></td>
    <td style="border:2px solid black;">43m 40.75s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">36f7e8fa0702</code></td>
    <td style="border:2px solid black;">2013-02-21 16:32</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">CFL: 0.32</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">0592f3835b5c</code></td>
    <td style="border:2px solid black;">24m 44.49s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">a1e3ead836eb</code></td>
    <td style="border:2px solid black;">2013-02-21 16:32</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">CFL: 0.64</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">0592f3835b5c</code></td>
    <td style="border:2px solid black;">17m 53.83s    </td>
  </tr>
</table>
<br>

### Grid Spacing

The figures show a comparison between ```Nx=1200``` (the red curves) and ```Nx=150, 300, 600```. ```Nx``` is the total number of cells from the bottom to the top of the domain including the length of the feature and the boundary layer. The results do not demonstrate any clear grid convergence at present and further results with finer grids are required. These runs are all in serial at present. Some changes are required to the level set implementation in FiPy to run in parallel to allow comparison with finer grids.  

<div class="highlight"><pre><code class="python"><span class="kn">from</span> <span class="nn">multiViewer</span> <span class="kn">import</span> <span class="n">MultiViewer</span>
<span class="kn">from</span> <span class="nn">smtext</span> <span class="kn">import</span> <span class="n">getSMTRecords</span><span class="p">,</span> <span class="n">CustomHTMLFormatter</span>

<span class="n">records</span> <span class="o">=</span> <span class="n">getSMTRecords</span><span class="p">(</span><span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;batch2&#39;</span><span class="p">])</span>
<span class="n">records</span> <span class="o">=</span> <span class="p">[</span><span class="n">getSMTRecords</span><span class="p">(</span><span class="n">records</span><span class="o">=</span><span class="n">records</span><span class="p">,</span> <span class="n">parameters</span><span class="o">=</span><span class="p">{</span><span class="s">&#39;Nx&#39;</span> <span class="p">:</span> <span class="n">Nx</span><span class="p">})[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">Nx</span> <span class="ow">in</span> <span class="p">(</span><span class="mi">1200</span><span class="p">,</span> <span class="mi">600</span><span class="p">,</span> <span class="mi">300</span><span class="p">,</span> <span class="mi">150</span><span class="p">)]</span>
<span class="n">title</span> <span class="o">=</span> <span class="p">[</span><span class="s">r&#39;Nx={0:d}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">r</span><span class="o">.</span><span class="n">parameters</span><span class="p">[</span><span class="s">&#39;Nx&#39;</span><span class="p">])</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">records</span><span class="p">[</span><span class="mi">1</span><span class="p">:]]</span>
<span class="n">viewer</span> <span class="o">=</span> <span class="n">MultiViewer</span><span class="p">(</span><span class="n">records</span><span class="p">[</span><span class="mi">1</span><span class="p">:],</span> <span class="n">baseRecords</span><span class="o">=</span><span class="n">records</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">title</span><span class="o">=</span><span class="n">title</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="mi">9</span><span class="p">))</span>
<span class="n">viewer</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">times</span><span class="o">=</span><span class="p">(</span><span class="mf">0.</span><span class="p">,</span> <span class="mf">1000.</span><span class="p">,</span> <span class="mf">2000.</span><span class="p">,</span> <span class="mf">3000.</span><span class="p">,</span> <span class="mf">4000.</span><span class="p">))</span>
<span class="n">CustomHTMLFormatter</span><span class="p">(</span><span class="n">records</span><span class="p">,</span> <span class="n">fields</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;label&#39;</span><span class="p">,</span> <span class="s">&#39;timestamp&#39;</span><span class="p">,</span> <span class="s">&#39;parameters&#39;</span><span class="p">,</span> <span class="s">&#39;repository&#39;</span><span class="p">,</span> <span class="s">&#39;version&#39;</span><span class="p">,</span> <span class="s">&#39;duration&#39;</span><span class="p">],</span> <span class="n">parameters</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;Nx&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">ipython_table</span><span class="p">()</span>
</code></pre></div>



![]({{ site.imageurl }}/extremefill2D_files/extremefill2D_fig_01.png)

<table style="border:2px solid black;border-collapse:collapse; font-size:10px;">
  <tr>
    <th style="border:2px solid black;background:#b5cfd2">Label</th>
    <th style="border:2px solid black;background:#b5cfd2">Timestamp</th>
    <th style="border:2px solid black;background:#b5cfd2">Parameters</th>
    <th style="border:2px solid black;background:#b5cfd2">Repository</th>
    <th style="border:2px solid black;background:#b5cfd2">Version</th>
    <th style="border:2px solid black;background:#b5cfd2">Duration    </th>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">143dec5e7ecd</code></td>
    <td style="border:2px solid black;">2013-02-28 11:48</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">Nx: 1200</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">81f76189d481</code></td>
    <td style="border:2px solid black;">5d 21h 57m 20.14s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">4282f5340892</code></td>
    <td style="border:2px solid black;">2013-02-28 11:51</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">Nx: 600</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">81f76189d481</code></td>
    <td style="border:2px solid black;">11h 8m 2.38s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">e66ca6267686</code></td>
    <td style="border:2px solid black;">2013-02-28 11:48</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">Nx: 300</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">81f76189d481</code></td>
    <td style="border:2px solid black;">1h 26m 11.63s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">85626d5b2715</code></td>
    <td style="border:2px solid black;">2013-02-28 11:51</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">Nx: 150</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">81f76189d481</code></td>
    <td style="border:2px solid black;">16m 39.49s    </td>
  </tr>
</table>
<br>

### Sweeps

<div class="highlight"><pre><code class="python"><span class="kn">from</span> <span class="nn">multiViewer</span> <span class="kn">import</span> <span class="n">MultiViewer</span>
<span class="kn">from</span> <span class="nn">smtext</span> <span class="kn">import</span> <span class="n">getSMTRecords</span><span class="p">,</span> <span class="n">CustomHTMLFormatter</span>

<span class="n">records</span> <span class="o">=</span> <span class="n">getSMTRecords</span><span class="p">(</span><span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;serialnumber4&#39;</span><span class="p">])</span>
<span class="n">records</span> <span class="o">=</span> <span class="p">[</span><span class="n">getSMTRecords</span><span class="p">(</span><span class="n">records</span><span class="o">=</span><span class="n">records</span><span class="p">,</span> <span class="n">parameters</span><span class="o">=</span><span class="p">{</span><span class="s">&#39;sweeps&#39;</span> <span class="p">:</span> <span class="n">sweeps</span><span class="p">})[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">sweeps</span> <span class="ow">in</span> <span class="p">(</span><span class="mi">32</span><span class="p">,</span> <span class="mi">16</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">)]</span>
<span class="n">title</span> <span class="o">=</span> <span class="p">[</span><span class="s">r&#39;sweeps={0:d}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">r</span><span class="o">.</span><span class="n">parameters</span><span class="p">[</span><span class="s">&#39;sweeps&#39;</span><span class="p">])</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">records</span><span class="p">[</span><span class="mi">1</span><span class="p">:]]</span>
<span class="n">viewer</span> <span class="o">=</span> <span class="n">MultiViewer</span><span class="p">(</span><span class="n">records</span><span class="p">[</span><span class="mi">1</span><span class="p">:],</span> <span class="n">baseRecords</span><span class="o">=</span><span class="n">records</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">title</span><span class="o">=</span><span class="n">title</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">9</span><span class="p">))</span>
<span class="n">viewer</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">times</span><span class="o">=</span><span class="p">(</span><span class="mf">0.</span><span class="p">,</span> <span class="mf">1000.</span><span class="p">,</span> <span class="mf">2000.</span><span class="p">,</span> <span class="mf">3000.</span><span class="p">,</span> <span class="mf">4000.</span><span class="p">))</span>
<span class="n">CustomHTMLFormatter</span><span class="p">(</span><span class="n">records</span><span class="p">,</span> <span class="n">fields</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;label&#39;</span><span class="p">,</span> <span class="s">&#39;timestamp&#39;</span><span class="p">,</span> <span class="s">&#39;parameters&#39;</span><span class="p">,</span> <span class="s">&#39;repository&#39;</span><span class="p">,</span> <span class="s">&#39;version&#39;</span><span class="p">,</span> <span class="s">&#39;duration&#39;</span><span class="p">],</span> <span class="n">parameters</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;sweeps&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">ipython_table</span><span class="p">()</span>
</code></pre></div>



![]({{ site.imageurl }}/extremefill2D_files/extremefill2D_fig_02.png)

<table style="border:2px solid black;border-collapse:collapse; font-size:10px;">
  <tr>
    <th style="border:2px solid black;background:#b5cfd2">Label</th>
    <th style="border:2px solid black;background:#b5cfd2">Timestamp</th>
    <th style="border:2px solid black;background:#b5cfd2">Parameters</th>
    <th style="border:2px solid black;background:#b5cfd2">Repository</th>
    <th style="border:2px solid black;background:#b5cfd2">Version</th>
    <th style="border:2px solid black;background:#b5cfd2">Duration    </th>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">7ed71a0a1faf</code></td>
    <td style="border:2px solid black;">2013-03-26 17:12</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">sweeps: 32</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">26a1c53dc79c</code></td>
    <td style="border:2px solid black;">3h 35m 47.96s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">7a17de0b7487</code></td>
    <td style="border:2px solid black;">2013-03-26 17:12</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">sweeps: 16</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">26a1c53dc79c</code></td>
    <td style="border:2px solid black;">3h 10m 54.34s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">8307dc417ea0</code></td>
    <td style="border:2px solid black;">2013-03-26 17:12</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">sweeps: 8</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">26a1c53dc79c</code></td>
    <td style="border:2px solid black;">1h 6m 16.29s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">e16fa2b84942</code></td>
    <td style="border:2px solid black;">2013-03-26 17:12</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">sweeps: 4</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">26a1c53dc79c</code></td>
    <td style="border:2px solid black;">1h 3m 56.60s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">528f07e88fae</code></td>
    <td style="border:2px solid black;">2013-03-26 17:12</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">sweeps: 2</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">26a1c53dc79c</code></td>
    <td style="border:2px solid black;">26m 3.20s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">331ce2cd522c</code></td>
    <td style="border:2px solid black;">2013-03-26 17:12</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">sweeps: 1</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">26a1c53dc79c</code></td>
    <td style="border:2px solid black;">15m 42.37s    </td>
  </tr>
</table>
<br>

### Linear Tolerance

<div class="highlight"><pre><code class="python"><span class="kn">from</span> <span class="nn">multiViewer</span> <span class="kn">import</span> <span class="n">MultiViewer</span>
<span class="kn">from</span> <span class="nn">smtext</span> <span class="kn">import</span> <span class="n">getSMTRecords</span><span class="p">,</span> <span class="n">CustomHTMLFormatter</span>

<span class="n">records</span> <span class="o">=</span> <span class="n">getSMTRecords</span><span class="p">(</span><span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;serialnumber7&#39;</span><span class="p">])</span>
<span class="n">records</span> <span class="o">=</span> <span class="p">[</span><span class="n">getSMTRecords</span><span class="p">(</span><span class="n">records</span><span class="o">=</span><span class="n">records</span><span class="p">,</span> <span class="n">parameters</span><span class="o">=</span><span class="p">{</span><span class="s">&#39;solver_tol&#39;</span> <span class="p">:</span> <span class="n">solver_tol</span><span class="p">})[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">solver_tol</span> <span class="ow">in</span> <span class="p">(</span><span class="mf">1e-7</span><span class="p">,</span> <span class="mf">1e-6</span><span class="p">,</span> <span class="mf">1e-5</span><span class="p">,</span> <span class="mf">1e-4</span><span class="p">,</span> <span class="mf">1e-3</span><span class="p">,</span> <span class="mf">1e-2</span><span class="p">,</span> <span class="mf">1e-1</span><span class="p">)]</span>
<span class="n">title</span> <span class="o">=</span> <span class="p">[</span><span class="s">r&#39;tol={0:1.1e}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">r</span><span class="o">.</span><span class="n">parameters</span><span class="p">[</span><span class="s">&#39;solver_tol&#39;</span><span class="p">])</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">records</span><span class="p">[</span><span class="mi">1</span><span class="p">:]]</span>
<span class="n">viewer</span> <span class="o">=</span> <span class="n">MultiViewer</span><span class="p">(</span><span class="n">records</span><span class="p">[</span><span class="mi">1</span><span class="p">:],</span> <span class="n">baseRecords</span><span class="o">=</span><span class="n">records</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">title</span><span class="o">=</span><span class="n">title</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">12</span><span class="p">,</span> <span class="mi">9</span><span class="p">))</span>
<span class="n">viewer</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">times</span><span class="o">=</span><span class="p">(</span><span class="mf">0.</span><span class="p">,</span> <span class="mf">1000.</span><span class="p">,</span> <span class="mf">2000.</span><span class="p">,</span> <span class="mf">3000.</span><span class="p">,</span> <span class="mf">4000.</span><span class="p">))</span>
<span class="n">CustomHTMLFormatter</span><span class="p">(</span><span class="n">records</span><span class="p">,</span> <span class="n">fields</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;label&#39;</span><span class="p">,</span> <span class="s">&#39;timestamp&#39;</span><span class="p">,</span> <span class="s">&#39;parameters&#39;</span><span class="p">,</span> <span class="s">&#39;repository&#39;</span><span class="p">,</span> <span class="s">&#39;version&#39;</span><span class="p">,</span> <span class="s">&#39;duration&#39;</span><span class="p">],</span> <span class="n">parameters</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;solver_tol&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">ipython_table</span><span class="p">()</span>
</code></pre></div>



![]({{ site.imageurl }}/extremefill2D_files/extremefill2D_fig_03.png)

<table style="border:2px solid black;border-collapse:collapse; font-size:10px;">
  <tr>
    <th style="border:2px solid black;background:#b5cfd2">Label</th>
    <th style="border:2px solid black;background:#b5cfd2">Timestamp</th>
    <th style="border:2px solid black;background:#b5cfd2">Parameters</th>
    <th style="border:2px solid black;background:#b5cfd2">Repository</th>
    <th style="border:2px solid black;background:#b5cfd2">Version</th>
    <th style="border:2px solid black;background:#b5cfd2">Duration    </th>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">faa5d9f206ed</code></td>
    <td style="border:2px solid black;">2013-03-27 11:25</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">solver_tol: 1e-07</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">a5790e469d66</code></td>
    <td style="border:2px solid black;">32m 58.14s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">f59dfdbec834</code></td>
    <td style="border:2px solid black;">2013-03-27 11:24</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">solver_tol: 1e-06</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">a5790e469d66</code></td>
    <td style="border:2px solid black;">33m 43.28s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">9bc8c7395961</code></td>
    <td style="border:2px solid black;">2013-03-27 11:24</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">solver_tol: 1e-05</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">a5790e469d66</code></td>
    <td style="border:2px solid black;">31m 14.05s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">417bcf854132</code></td>
    <td style="border:2px solid black;">2013-03-27 11:24</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">solver_tol: 0.0001</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">a5790e469d66</code></td>
    <td style="border:2px solid black;">27m 41.94s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">33b8c8063ac2</code></td>
    <td style="border:2px solid black;">2013-03-27 11:24</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">solver_tol: 0.001</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">a5790e469d66</code></td>
    <td style="border:2px solid black;">25m 56.36s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">5ad7bdc1a530</code></td>
    <td style="border:2px solid black;">2013-03-27 11:24</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">solver_tol: 0.01</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">a5790e469d66</code></td>
    <td style="border:2px solid black;">31m 59.05s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">2531d84308b4</code></td>
    <td style="border:2px solid black;">2013-03-27 11:24</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">solver_tol: 0.1</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">a5790e469d66</code></td>
    <td style="border:2px solid black;">1h 6m 29.66s    </td>
  </tr>
</table>
<br>

## Control Parameters

Using the images above, the control parameters will be adjusted from

```
sweeps = 30
solver_tol = 1e-6
CFL = 0.1
tol = 1e-1```

to

```
sweeps = 4
solver_tol = 1e-10
CFL = 0.1
tol = 1e-10```

Using these new parameters, simulations have been run with ```Nx=150, 300, 600``` and compared with the old parameters. Simulations with the new parameters are more efficient without sacrificing accuracy.


<div class="highlight"><pre><code class="python"><span class="kn">from</span> <span class="nn">multiViewer</span> <span class="kn">import</span> <span class="n">MultiViewer</span>
<span class="kn">from</span> <span class="nn">smtext</span> <span class="kn">import</span> <span class="n">getSMTRecords</span><span class="p">,</span> <span class="n">CustomHTMLFormatter</span>

<span class="n">Nxs</span> <span class="o">=</span> <span class="p">(</span><span class="mi">600</span><span class="p">,</span> <span class="mi">300</span><span class="p">)</span>
<span class="n">records</span> <span class="o">=</span> <span class="n">getSMTRecords</span><span class="p">(</span><span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;serialnumber8&#39;</span><span class="p">])</span>
<span class="n">records</span> <span class="o">=</span> <span class="p">[</span><span class="n">getSMTRecords</span><span class="p">(</span><span class="n">records</span><span class="o">=</span><span class="n">records</span><span class="p">,</span> <span class="n">parameters</span><span class="o">=</span><span class="p">{</span><span class="s">&#39;Nx&#39;</span> <span class="p">:</span> <span class="n">Nx</span><span class="p">})[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">Nx</span> <span class="ow">in</span> <span class="n">Nxs</span><span class="p">]</span>
<span class="n">baseRecords</span> <span class="o">=</span> <span class="n">getSMTRecords</span><span class="p">(</span><span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;batch2&#39;</span><span class="p">])</span>
<span class="n">baseRecords</span> <span class="o">=</span> <span class="p">[</span><span class="n">getSMTRecords</span><span class="p">(</span><span class="n">records</span><span class="o">=</span><span class="n">baseRecords</span><span class="p">,</span> <span class="n">parameters</span><span class="o">=</span><span class="p">{</span><span class="s">&#39;Nx&#39;</span> <span class="p">:</span> <span class="n">Nx</span><span class="p">})[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">Nx</span> <span class="ow">in</span> <span class="n">Nxs</span><span class="p">]</span>
<span class="n">title</span> <span class="o">=</span> <span class="p">[</span><span class="s">r&#39;Nx={0:d}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">r</span><span class="o">.</span><span class="n">parameters</span><span class="p">[</span><span class="s">&#39;Nx&#39;</span><span class="p">])</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">records</span><span class="p">]</span>
<span class="n">viewer</span> <span class="o">=</span> <span class="n">MultiViewer</span><span class="p">(</span><span class="n">records</span><span class="p">,</span> <span class="n">baseRecords</span><span class="o">=</span><span class="n">baseRecords</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="n">title</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">9</span><span class="p">))</span>
<span class="n">viewer</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">times</span><span class="o">=</span><span class="p">(</span><span class="mf">0.</span><span class="p">,</span> <span class="mf">1000.</span><span class="p">,</span> <span class="mf">2000.</span><span class="p">,</span> <span class="mf">3000.</span><span class="p">,</span> <span class="mf">4000.</span><span class="p">))</span>
<span class="n">CustomHTMLFormatter</span><span class="p">(</span><span class="n">records</span> <span class="o">+</span> <span class="n">baseRecords</span><span class="p">,</span> <span class="n">fields</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;label&#39;</span><span class="p">,</span> <span class="s">&#39;timestamp&#39;</span><span class="p">,</span> <span class="s">&#39;parameters&#39;</span><span class="p">,</span> <span class="s">&#39;repository&#39;</span><span class="p">,</span> <span class="s">&#39;version&#39;</span><span class="p">,</span> <span class="s">&#39;duration&#39;</span><span class="p">],</span> <span class="n">parameters</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;Nx&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">ipython_table</span><span class="p">()</span>
</code></pre></div>



![]({{ site.imageurl }}/extremefill2D_files/extremefill2D_fig_04.png)

<table style="border:2px solid black;border-collapse:collapse; font-size:10px;">
  <tr>
    <th style="border:2px solid black;background:#b5cfd2">Label</th>
    <th style="border:2px solid black;background:#b5cfd2">Timestamp</th>
    <th style="border:2px solid black;background:#b5cfd2">Parameters</th>
    <th style="border:2px solid black;background:#b5cfd2">Repository</th>
    <th style="border:2px solid black;background:#b5cfd2">Version</th>
    <th style="border:2px solid black;background:#b5cfd2">Duration    </th>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">d83505552902</code></td>
    <td style="border:2px solid black;">2013-03-27 14:22</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">Nx: 600</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">a5790e469d66</code></td>
    <td style="border:2px solid black;">4h 20m 30.13s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">8cdf3a35f80f</code></td>
    <td style="border:2px solid black;">2013-03-27 14:22</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">Nx: 300</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">a5790e469d66</code></td>
    <td style="border:2px solid black;">28m 45.72s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">4282f5340892</code></td>
    <td style="border:2px solid black;">2013-02-28 11:51</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">Nx: 600</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">81f76189d481</code></td>
    <td style="border:2px solid black;">11h 8m 2.38s    </td>
  </tr>
  <tr>
    <td style="border:2px solid black;"><code style="font-size:10px;">e66ca6267686</code></td>
    <td style="border:2px solid black;">2013-02-28 11:48</td>
    <td style="border:2px solid black;"><code style="font-size:10px;">Nx: 300</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">/users/wd15/git/extremefill-data (git@github.com:wd15/extremefill-data.git)</code></td>
    <td style="border:2px solid black;"><code style="font-size:10px;">81f76189d481</code></td>
    <td style="border:2px solid black;">1h 26m 11.63s    </td>
  </tr>
</table>
