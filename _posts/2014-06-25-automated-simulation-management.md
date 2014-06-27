---
layout: post
title: "Automated Simulation Management"
category: posts
---

I gave my wife a Fitbit as a holiday gift and she really likes it. An
unfortunate consequence of her enthusiasm is that we often end up
heading off on a cold winter's night to the local grocery store, where
we power walk up and down the aisles until she reaches the magic
10,000 steps that indicate that she has exercised enough to satisfy
the device and receive awards for her effort from the Fitbit
website. Aside from the small inconvenience of having to rush around
Wegman's late at night as the clerks give us strange looks, the Fitbit
is a wonderful device. It records the number of steps taken each day,
one's weight (with the purchase of the accessory, somewhat pricey
scales), sleep, vertical steps and more. The results are stored in the
cloud and presented on a website with upbeat graphics that render the
data easily digestible.

Considering the technology available for data capture in our daily
lives, the scientific process seems increasingly moribund in
comparison. My everyday workflow often consists of running multiple
numerical simulations for multiple projects. Up until recently, I kept
records of these simulations using mostly manual and entirely ad-hoc
schemes. Intuitively, one would imagine that maintaining simulation
records for computational processes would be a relatively
straightforward problem. After all this is a deterministic process
existing entirely in silico and is seemingly much simpler than
recording in vivo/vitro as with the Fitbit or an experimental
apparatus. In practice, I have found maintaining ad-hoc schemes to
manage simulations to be very difficult and often results in a
fast degradation of the data after a project has ended.

It seems mystifying to me as to why there are not at least a
half-dozen well supported open source projects that address the issues
surrounding simulation management, let alone web frameworks that would
support the cloud storage, sharing and versioning of simulation
meta-data. I can say with some conviction that scientists have sleep
walked through the last 10 years of web technology. It is high time to
take a step back from research and concentrate on building the web
infrastructure needed to improve the scientific process especially in
the realm of scientific computing.

## Workflow, Version Control and Event Control

I think it is important to be clear at this point that I do not
advocate for an all encompassing workflow tool that presumes to manage
every aspect of one's scientific life, but really just a tool to deal
with event control. Event control is very different from version
control or workflow.  Event control is the versioning and capture of
meta-data to do with the the execution of a workflow (or just a script
or computer program). Event control shares many similarities with
version control, but records different types of meta-data at each
*commit*. Git is a simple, robust command line tool for version
control. It forms a platform for many other high level tools and web
services (e.g. VisTrails, Github). In my mind, to start leveraging web
infrastructure and fancy cloud services for data provenance, a tool
along the same lines as Git is required for event control.

## Data and Meta-Data

Another important issue to take note of is the distinction between
meta-data about simulations and output data produced by
simulations. The rant in this blog post relates to the versioning,
capture and sharing of meta-data about simulations not the actual data
produced by the simulations. The provenannce of meta-data is, in
principle, a much easier problem to deal with than the output data
provenance problem that is often raised in discussions about
reproducible research. For one thing, the size of the meta-data is
inconsequential compared with the output data. It is also much easier
to develop simple protocols and standards for meta-data. I
acknowledge that provenance issues surrounding simulation output data
is hugely important, but the data issue can't really be tackled
effectively until the meta-data issue is resolved.

## Reproducible Research

The following figure is an idealized schematic showing the five stages
of progress during a computational research project.

!image()

In many ways, the last two stages of this process are quite easy to
make reproducible assuming one can access the simulation output data
(another story). Version control helps with all these stages, but is
especially useful during the development stage. Presumably there is no
need to capture much provenance data during the the prototyping and
development stage. There is no real need for these stages to be
formally reproducible. The simulation stage is where current practices
really need to be improved. This after all is the most important part
of any project with respect to reproducible research. It is the actual
execution of the experiment as opposed to the assembling of the
apparatus or the figure rendering in a paper. In the simulation stage,
assuming that we have a well developed code base and we are just
investigating parameters (and maybe only tweaking the code), we are
now ideally in a mode of working that is well defined and is tractable
to event control and meta-data capture.

## Sumatra

Over the last year I've become very interested in the Sumatra project,
it is beginning to answer a lot of the issues sorroungdin capture of
meta-data in simulations. If you are interested in using Sumatra check
out the docs. I also have a IPython notebook demoing it with Pandas,
showing how to import the meta-data as a Pandas dataset.

Sumatra has to reach a critical mass of users.  A lot of issues need
to be addressed (if face there are X on the issues tracker alon)
It underuntilized and therfore it is quite buggy. WE must try and
incease it's use and a lot more of the issues will get worked on

However, Sumatar deals with the main issue of capturing the
meta-data. This project really needs more community support as well as
some competing projects that address the same issues. 

There are many limitations with Sumatra. I won't go into them all. I don' want to sound
too negative more that this project needs more community support, but
it really is a nice idea and I use it every time I run any simulation.

What is really exciting is that the main author of Sumara has now
started with sumartra-server, splitting off the developmen into a
client server model. This is wonderful, but the tools needs a lot of
work on the basics. As I said above, we must A before we can B.

## Cloud Service

C. Titus Brown mentioned two things in a blog post, the following 

 * 



## What can NIST do?

I was prompted to do this blog post as I an part of a focus group
called "weathering the data storm" at the National Institute of
Standards and Technology. The group aims to provide some
reccomendations to upper managment about the direction NIST needs to
take in dealing with workflow, reprocucitibiely, data captutre,
provenec issues and all that fine stuff. The remit also include
physical infrastructue for scientific data, but I have less interest
in that side of things. From my perspective the role that NIST could
paly in improving data provence would be.

 * In general, more active engagment and support for open source
   projects that are already trying to answer the issues around data
   capture and provence. This support should include grant money for
   these projects. Upper management also needs to be supportive of
   NIST staff members who take time to activley engage with the the
   open source community.
   
 * Really start thinking seriously about hosting cloud services for
   the general commuingity. This should include services for automated
   data provence as this is severlky lacking at the moment and is low
   hanging fruit in a number of ways. This raised the question of yhy
   aren't the goverment (and by extension NIST) hasn't hosted or
   developed some of the services for academic data or workflow that
   already exist such as Figshare, Wakari or Aurhtorea. Maybe the
   goverment isn't the right venue for these, I don't really know, but
   it seems strange albeit from my naive understanding.

## Conclusion

From my standpoint, the
effective cloud-based simulation management is the most important
issue in making scientific computing more reproducible in my own field
of materials science.


