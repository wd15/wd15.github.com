---
layout: post
title: "Automated Simulation Management"
category: posts
---

My wife was delighted when I gave her a Fitbit as a holiday gift. An
unfortunate consequence of her continued enthusiasm is that we often
end up heading out on a cold winter's night to the local grocery
store, where we power walk up and down the aisles until she reaches
the magic 10,000 steps -- indicating that she has exercised enough to
satisfy the Fitbit gods. Aside from the small inconvenience of having
to rush around Wegman's late at night as the staff there give us
perplexed looks, the Fitbit is a wonderful device. It records the
number of steps taken each day, one's weight (with the purchase of the
accessory, somewhat pricey, scales), sleep, vertical steps and
more. The results are stored in the cloud and presented on a website
with upbeat graphics that render the data easily digestible.

Considering the technology available for data capture in our daily
lives, the scientific process seems increasingly moribund in
comparison. My everyday workflow often consists of running multiple
numerical simulations for multiple projects. Up until recently, I kept
records of these simulations using mostly manual and entirely ad hoc
schemes. Intuitively, one would imagine that maintaining simulation
records for computational processes would be a relatively
straightforward problem. After all this is a deterministic process
existing entirely in silico and is seemingly much simpler than
recording in vivo/vitro as with the Fitbit or an experimental
apparatus. In practice, I have found that managing numerical
simulation using ad hoc schemes to be a maintenance nightmare. In
particular, ad hoc schemes result in fast degradation of data after
projects end.

I am mystified as to why there are not at least a half-dozen well
supported, open source projects that address the issues surrounding
simulation management. Web frameworks that support cloud storage,
sharing and versioning of simulation metadata should be commonplace. I
can say with some conviction that scientists have sleepwalked through
the last 10 years of web technology. It is high time to take a step
back from research and concentrate on building the tools and web
infrastructure needed to improve the scientific process, especially in
the realm of scientific computing.

## Workflow, Version Control and Event Control

I think it is important to be clear at this point that I do not
advocate for an all encompassing workflow tool that presumes to manage
every aspect of one's scientific life, but really just a tool to deal
with event control. Event control is very different from version
control or workflow.  Event control is the versioning and capture of
metadata to do with the execution of a workflow (or just a script or
computer program). Event control shares many similarities with version
control, but records different types of metadata at each
*commit*. Git is a simple, robust command line tool for version
control. It forms a platform for many other high level tools and web
services (e.g. VisTrails, Github). In my mind, to start leveraging web
infrastructure and fancy cloud services for data provenance, a tool
along the same lines as Git is required for event control.

## Data and Metadata

Another important issue to take note of is the distinction between
metadata about simulations and output data produced by
simulations. The rant in this blog post relates to the versioning,
capture and sharing of metadata about simulations not the actual data
produced by the simulations. The provenance of metadata is, in
principle, a much easier problem to deal with than the output data
provenance problem that is often raised in discussions about
reproducible research. For one thing, the size of the metadata is
inconsequential compared with the output data. It is also much easier
to develop simple protocols and standards for metadata. I acknowledge
that provenance issues surrounding simulation output data is hugely
important, but the data issue can't really be tackled effectively
until the metadata issue is resolved.

## Reproducible Research

The following figure is an idealized schematic showing the five stages
of progress during a computational research project.

![scientific progress](https://raw.githubusercontent.com/wd15/diffusion-workshop-2014/94733caf39782e4f905b744e99bd9aac498344cb/images/workflow.png)

In many ways, the last two stages of this process are quite easy to
make reproducible assuming one can access the simulation output data
(another story). Version control helps with all these stages, but is
especially useful during the development stage. Presumably there is no
need to capture much provenance data during the prototyping and
development stage. There is no real need for these stages to be
formally reproducible. The simulation stage is where current practices
really need to be improved. This after all is the most important part
of any project with respect to reproducible research. It is the actual
execution of the experiment as opposed to the assembling of the
apparatus or the figure rendering in a paper. In the simulation stage,
assuming that we have a well developed code base and we are just
investigating parameters (and maybe only tweaking the code), we are
now ideally in a mode of working that is well defined and is tractable
to event control and metadata capture.

## Sumatra

Over the last year I've become very interested in the Sumatra project,
it is beginning to answer some of the issues sorrounding the
versioning and capture of metadata for simulations. Please do take a
look at this project and try to use it if fits with your own workflow,
especially if you are an avid Python user. I have an IPython notebook
demonstraing the use of Sumatra for simple parallel problem and mixing
metadata records and output results with Pandas. The single most
important issue for Sumatra is to reach a ctirical mass of users. The
many issues on the tracker (X issues tracker alone) will only be
addressed if the project reaches critical mass. I now use Sumatra for
all my simulation management and try to fix bugs and contribute back
to the project whenever I can.

## Cloud Service

I noticed recently that the main developer of Sumatra is now working
on Sumatra-server. I'm excited that this might form the basis for a
client-server model for Sumatra and an eventual cloud service for
simulation management. Such a service would lead to improved sharing
of data, improved reproducible simulation results and then the
eventual promised land of aggregation and analytics of metadata (and
possibly output data) across disparate research projects.

To elucidate the value a could service for simulation management could
provide, I would like to raise two of the ideas mentioned in
[C. Titus Brown's blog post](http://ivory.idyll.org/blog/2014-imagine.html)
about reproducible research. These are:

 * "a declarative metadata standard that you can use to tell a Linux
   VM how to download your data"

 * "automated integration tests for papers."

These ideas are at the heart of making simulations truly
reproducible. I believe that the client-server model of Sumatra can
meet these two requirements. Regarding the first point: the tool that
automatically captures the metadata and has the ability to rebuild an
environment based on that metadata will become the defacto metadata
standard. For the second point: Sumatra already records the hash for
output data files and has the functionality to rerun simulations and
check that the hash matches thereby forming a coarse level regression
test. Furthermore, integration of Sumatra with Buildbot would allow
this process to be entirely automated whenever a repository is
updated.

## What can NIST do to help?

I am part of the Data Storm Focus Group in the Materials Measurement
Laboratory at the National Institute of Standards and Technology
(NIST). The group aims to provide recommendations to upper management
on the direction NIST needs to take in weathering the future data
storm. In particular the group will make recommendations on issues
such as workflow management, reproducible research and data provenance
issues. The group has also discussed physical infrastructure for
scientific data though I have less interest in that area. From my
perspective, some important actions NIST can take in the area of
improving data management include:

 * More active engagement with open source projects that are already
   answering the issues surrounding data capture and provenance.

 * Reward NIST staff members that are actively supporting the open
   source community, especially widely used projects that have
   primary developers external to NIST.
   
 * Take a less NIST-centred viewpoint about cloud services and open
   source projects. Open source projects are no longer associated with
   a particular institution.
 
 * Start thinking seriously about hosting cloud services for the
   general community including automated data provenance (this is low
   hanging fruit in a number of ways and the next frontier in
   scientific data management). This raises the question of why aren't
   the government (and by extension NIST) hosting some of the services
   for academic data or workflow that already exist such as
   [Figshare](http://figshare.com), [Wakari](https://www.wakari.io/)
   or [Authorea](https://authorea.com/). Maybe the government isn't
   the right venue for these, I really don't know, but it seems
   strange albeit from my naive position.

 * Seek out workflow or data based open source projects that are
   currently being used widely at NIST (such as
   [IPython](http://ipython.org/)) and give grant money to the
   developers. There are multiple benefits to NIST in this approach
   including the possibility to influence these projects to meet NIST
   and the wider community's needs without any large investments.

## Conclusion

From my standpoint, we are on the cusp of a revolution in scientific
data management, which will greatly improve scientific research,
reproducible science and analytics across disparate research
projects. In my own corner, an important first step in this revolution
is the development of effective cloud-based simulation record keeping
and management. Personally, it would be fun to be a part of this
revolution in some way by making small contributions to projects such
as Sumatra. in the big picture, NIST really needs to be at the center
of supporting and providing cloud services and software tools for
varying scientific communities in order to remain relevant in the new
data revolution.

Please see the slides from a talk I gave on
[Managing Numerical Simulations](http://wd15.github.io/diffusion-workshop-2014)
at the NIST Diffusion Workshop.

