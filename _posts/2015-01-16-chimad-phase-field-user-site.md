---
layout: post
title: "CHiMaD - Phase Field User Site"
category: posts
---

## Workshop 01/09/2015

Last week I attended the Phase Field Methods Workshop at Northwestern
University,
[see the PDF document about the meeting](https://drive.google.com/file/d/0B4101gT3tHveaGhmajZ4cE1fQWM/view?usp=sharing). The
meeting was really aimed at finding ways to unify the effort in
developing computational tools for phase field simulations and
especially to reduce replicated effort. The main actionable item that
came out of the meeting was a requirement for a focused web presence
for meta analysis and discussion of the various phase field codes
available. The general consensus was that a GitHub presence for the
community could serve this purpose. It was suggested that the NIST
contingent take charge of this item along with the some of the initial
contributions.

## Aims

What are the aims of a GitHub site for the phase field community:

 * location to create and collate data comparing code capabilities

 * location to finalize a set of canonical phase field examples
 
 * location to push scripts, recipes (IPython notebooks for example)
   for building and running phase field codes that solve the canonical
   examples (or any other phase field examples)

 * location for links to virtual machines for phase field codes
 
 * location to store phase field meta analysis on such things as
   efficiency (memory use), convergence, capabilities or ease of use

 * location for any phase field code that has no home elsewhere
   including student's phase field codes or phase field analysis

 * eventual location of meta analysis tools for automated testing of
   multiple phase field codes

 * eventual location of a generic high level API to describe phase
   field problems with hooks into multiple codes

I should add the caveat that the above is probably biased in favor of
some of my own ideas rather than ideas from all suggestions at the
meeting.

## Setting up the GitHub site

Of course we could just create a GitHub organization with the name
"chimad_phase_field" and have unlimited public repositories. It's
free. However, my NIST based colleagues were fairly sure that we
should create this organization within the "usnistgov"
organization. This raises the question of whether sub-organizations
can be created in GitHub. I'm unsure about this currently.

A second point of discussion was whether we needed an organization at
all or just a repository. From my perspective a single repository is
really not going to handle the kind of contributions that we are
interested in (multiple codes maybe, different disconnected
meta-analyses). The alternative is to just have a team and have
multiple repositories connected with the team as a poor man's
organization. This may work failing all else.

Before setting this up, I'm awaiting the input of several NIST
colleagues in order to see what direction we should go in and whether
I'm officially allowed to set up a GitHub organization external to
NIST.

## Mailing List

One item that we should deal with in short order is the creation of a
mailing list. The choices are:

 * NIST based mailing list (colleagues like this idea, I'm not enthusiastic)

 * Google Group (I'm more in favor, it's easier to setup and archive easily)

A mailing list for the community is really important.

## Some other links along similar lines

 * [Rosetta Code](http://rosettacode.org/wiki/Rosetta_Code)


