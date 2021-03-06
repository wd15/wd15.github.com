---
layout: post
title: "What is Extreme Fill?"
description: ""
category: 
tags: []
---

Extreme fill theory explains one particular mechanism of feature
filling in electroplating. The mechanism that results in extreme fill
is similar in a number of respects to both the
[curvature enhanced accelerator coverage](http://www.ctcms.nist.gov/fipy/examples/levelSet/electroChem/README.html)
(CEAC) and leveling mechanisms, which are both modulated by additives
in the electrolyte. In contrast to the CEAC and leveling mechanisms,
the defining characteristic of extreme fill is the highly segregated
deposition that occurs only on the very bottom of the feature with a
complete absence of deposition on the top surface and walls of the
feature. The image below of deposition in a silicon via demonstrates
just how segregated extreme fill can be.

<img src="{{site.imageurl}}/extremefill.png" alt="Drawing" style="width: 400px;"/>

The simplest explanation of extreme fill requires just two equations,
an equation for the deposition rate, $$v$$, given by

$$v = v_0 \left(1 - \theta\right)$$

and an equation for the coverage of an adsorbed additive (known as the
suppressor) at the electrode/electrolyte interface, $$\theta$$, given
by

$$ \dot{\theta} = k^+ c_{\theta} \left(1 - \theta\right) - k^- \theta v $$

where $$\theta$$ varies between 0 (no suppression) and 1 (fully
suppressed). The coverage of suppressor is governed by the competition
between adsorption and consumption controlled by $$k^+$$ and $$k^-$$,
respectively. The concentration of suppressor in the bulk electrolyte
is given by $$c_{\theta}$$.

There are two steady state solutions to these equations,
$$\theta=\frac{k^+ c_{\theta}}{k^- v_0}$$ and $$\theta=1$$. These two
states corresponding to the "on" and "off" states of deposition, which
manifests in the extreme fill behavior demonstrated in the image. Now,
if $$\frac{k^+ c_{\theta}}{k^- v_0} > 1$$ then the stable solution is
$$\theta=1$$, but if $$\frac{k^+ c_{\theta}}{k^- v_0} < 1$$, the
stable solution is given by
$$\theta=\frac{k^+c_{\theta}}{k^-v_0}$$. The control parameter here is
$$c_{\theta}$$, which varies spatially and can change rapidly
descending down the trench and thus enables an "off" state at the top
of the trench and an "on" state at the bottom of the trench.
To reach these steady "on" and "off" states, the equation for the
electric potential must also be coupled into the problem (see the full
set of equations on the
[extreme fill website](http://wd15.github.io/extremefill/#extremefill.simulation.Simulation)).

The movie below is generated by a pseudo steady state model of extreme
fill outlined in [this recent paper][paper]. It shows the normalized
potential (cyan), bulk suppressor concentration (green), cupric
concentration (red) and suppressor coverage (blue). The region where
$$x < 0$$ $$\mu$$m corresponds to the inside of the feature. When the
steady state is obtained, deposition is only occurring at the very
bottom of the feature $$x < 50$$ $$\mu$$m where the blue line is less
than 1 and bulk suppressor concentration (green line) is very close to
zero.

<p style="text-align: center;"><iframe width="480" height="360" src="http://www.youtube.com/embed/opkPA4mXFr4?rel=0" frameborder="0"> </iframe></p>

For further details about the extreme fill mechanism see
[the paper][paper], which contains a complete description of the
psuedo steady-state model. The
[extreme fill website](http://wd15.github.io/extremefill/) and
corresponding [Github repository](https://github.com/wd15/extremefill)
contain the necessary documentation and code to run the
[FiPy](http://www.ctcms.nist.gov/fipy/) model of extreme fill as well
as generate the data to completely reproduce the images in [the paper][paper].

 [paper]: http://dx.doi.org/10.1149/2.009210jes
