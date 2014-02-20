---
layout: post
title: "Parallel FiPy in IPython"
category: posts
---

I recently created
[two notebooks](http://nbviewer.ipython.org/github/wd15/fipy-efficiency/tree/master/notebooks/)
showing the performance of FiPy in parallel. The aim of the notebooks
is

 * to clearly demonstrate that FiPy scales reasonably well in parallel at
   least up to 48 nodes,
 
 * demonstrate that the differences between PySparse and Trilinos are
   not that important for larger problems,
   
 * have some publicly available data for FiPy's performance in parallel and 
 
 * to demonstrate the use of FiPy with IPython's native parallel
   infrastructure (still MPI based).

The
[first notebook](http://nbviewer.ipython.org/github/wd15/fipy-efficiency/blob/master/notebooks/FiPy-IPython.ipynb)
demonstrates how to use IPython's native parallel infrastructure with
FiPy and present parallel results on a laptop. The
[second notebook](http://nbviewer.ipython.org/github/wd15/fipy-efficiency/blob/master/notebooks/cluster.ipynb)
presents results for up to 48 parallel nodes running on a cluster.
   
