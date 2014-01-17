---
layout: post
title: "MKS Workshop"
category: posts
---

On January 13th and 14th we held a small workshop in the
[Center for Theoretical and Computational Materials Science (CTCMS)](http://www.nist.gov/mml/ctcms/)
at NIST to discuss and participate in working on materials informatics
code examples. We focused on the
[materials knowledge system (MKS)](http://nbviewer.ipython.org/github/wd15/pymks/blob/master/notebooks/02%20-%20MKS%20Intro.ipynb)
and the more general topic of spatial statistics. The MKS is a
regression technique that matches a microstructure with a response and
is a nice introduction to materials informatics and naturally leads
into other topics such as spatial statistics and machine learning. The
workshop consisted of
[lightning talks](https://github.com/wd15/pymks/wiki/Workshop-Schedule#lightning-talks)
given by a number of participants and tutorials given by me
([Daniel Wheeler](http://localhost:4000/about.html)) and
[Tony Fast](http://mined.gatech.edu/the-ga-tech-mined-research-group/ga-tech-mined-research-group-tony-fast).
There were also talks by
[Jim Warren](http://www.nist.gov/mml/james-warren.cfm) and
[Surya Kalidindi](https://github.com/wd15/pymks/wiki/Workshop-Schedule#surya-kalidindi-talk). While
the focus of the workshop was on materials informatics, the aim was
really to work on some of the scientific computing aspects of
materials informatics rather than the theoretical or experimental
aspects.

Overall I enjoyed the two days. I learned a lot about how to structure
this type of "hands on" workshop, more on that below. I have a better
idea of the global picture of how materials informatics relates to
spatial statistics and signal-response theory. I think that the
workshop has raised interest among a number of people from
conversations I've had with participants. In particular, it has
increased the understanding of how the MKS can augment existing
modeling techniques. Also, I think there is some future collaboration
with Tony that seems to be within reach, for example,

 - port the spatial statistics functions from Matlab to Python and
   then package and document,
 
 - create a nice set of examples that work as both demonstrations and
   regression tests.

### Criticism

I'll stick to my own experiences during my tutorial. I really enjoyed
doing it and especially preparing the materials. The tutorial was
prepared as a set of IPython notebooks with optional exercise
problems. From a Python perspective, addressing the audience was quite
difficult being made up of both very experienced Python users and
complete beginners. This is an almost impossible gap to bridge. On top
of this, I am new to the subject matter and haven't presented it
before.

The main issue with the tutorial was that no one really participated
in actually running the code and attempting the exercise
problems. This wasn't a show stopper and participants still got a lot
out of it. It just makes it more difficult to follow along and
understand each step in the coding process. With this in mind, here
are some ideas that would substantially improve subsequent tutorials.

 - Don't do it alone. Two people should really tutor for a 3 hour
   tutorial.

 - The first few exercise problems need to be really easy at first so
   that the material doesn't seem overly intimidating.

 - In this tutorial there were quite a few issues with the
   computational environment. These issues are completely negated with
   a cloud based environment using either
   [Wakari](https://www.wakari.io/) or a custom AMI.
 
 - Participants need to be able to see their screens and see the main
   screen without turning around.
 
 - Any tricky packages should have imports only in the cells or
   functions where they are used. This prevents pointless import
   errors that don't matter for most of the notebooks. This problem
   threw a few people right at the beginning.
 
 Specifically, when presenting the MKS.

 - Make the introduction far less dense and introduce the equations
   slowly defining each term and show lots of examples.
 
 - No need to have a Python intro. Any Python material can be embedded
   in the other tutorials.
   
 - Motivate why we are using the MKS. In this case to speed up solving
   an equation in a non-traditional way.

### Materials for MKS Tutorial

The materials for the MKS tutorial are available on Github

[https://github.com/wd15/pymks/tree/workshop](https://github.com/wd15/pymks/tree/workshop)

The IPython notebooks are viewable straight from the browser (without
Python or IPython installed on your computer)

[http://nbviewer.ipython.org/github/wd15/pymks/tree/workshop/notebooks/](http://nbviewer.ipython.org/github/wd15/pymks/tree/workshop/notebooks/)

### Materials for Spatial Statistics Tutorials

All of Tony's Matlab materials are also available at both

[https://github.com/tonyfast/SpatialStatisticsFFT](https://github.com/tonyfast/SpatialStatisticsFFT)

and

[https://github.com/tonyfast/NIST_MS_Workshop](https://github.com/tonyfast/NIST_MS_Workshop)


