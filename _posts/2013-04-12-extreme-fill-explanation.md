---
layout: post
title: "What is Extreme Fill?"
description: ""
category: 
tags: []
---
{% include JB/setup %}

Extreme fill is a theory that explains one particular mechanism of
feature filling in electroplating. It is similar in a number of
respects to both the
[curvature enhanced accelerator coverage](http://www.ctcms.nist.gov/fipy/examples/levelSet/electroChem/README.html)
(CEAC) and leveling mechanisms, which are both modulated by additives
in the electrolyte. In contrast to the CEAC and leveling mechanisms,
the defining characteristic of extreme fill is highly segregated
deposition occurring only on the very bottom of the feature with a
complete absence of deposition on the top surface and walls of the
feature. The image below of deposition in a silicon via demonstrates
just how segregated extreme fill can be.

<img src="/images/extremefill.png" alt="Drawing" style="width: 400px;"/>

The simplest explanation of extreme fill requires just two equations,
an equation for the current density $$i$$, given by

$$v = v_0 \left(1 - \theta\right)$$

and an equation for the coverage of an additive (known as the
suppressor), $$\theta$$, at the electrode/electrolyte interface, given
by

$$ \dot{\theta} = k^+ c_{\theta} \left(1 - \theta\right) - k^- \theta i $$

where $$\theta$$ varies between 0 (no suppression) and 1 (fully
suppressed). The adsorption rate of suppressor is governed by
competition between adsorption and consumption controlled by $$k^+$$
and $$k^-$$, respectively. The concentration of suppressor in the bulk
electrolyte is given by $$c_{\theta}$$.

There are always two steady state solutions to these equations,
$$\theta=\frac{k^+ c_{\theta}}{k^- v_0}$$ and $$\theta=1$$. These two
states corresponding to the "on" and "off" states of deposition, which
manifests in the extreme fill behavior demonstrated in the image. Now,
if $$\frac{k^+ c_{\theta}}{k^- v_0} > 1$$ then the stable solution is
$$\theta=1$$, but if $$\frac{k^+ c_{\theta}}{k^- v_0} < 1$$, the
stable solution is given by
$$\theta=\frac{k^+c_{\theta}}{k^-v_0}$$. The control parameter here is
$$c_{\theta}$$, which varies spatially and can change rapidly
descending down the trench and thus enable an "off" state at the top
of the trench and an "on" state at the bottom of the trench.

To reach these steady "on"/"off" states, the equation for the electric
potential must be coupled into to the problem see the full (set of
equations on the extreme fill website).  The movie below is generated
from a steady-state pseudo 2D model of extreme fill outlined in this
recent paper. It shows the normalized potential $\bar{\eta}$ (cyan),
the bulk suppressor concentration $\bar{c}_{\text{\theta}}$ (green),
the cupric concentration $\bar{c}_{\text{cu}}$ (red) and the
suppressor coverage $\theta$ (blue). The region where $x < 0$
corresponds to the inside of the feature. When the steady state is
obtained, deposition is only occurring at the very bottom of the feature
where the blue line is below 1.

<iframe width="480" height="360" src="http://www.youtube.com/embed/qE9fYpUG3TU" frameborder="0"> </iframe>

For further details about the extreme fill mechanism see the paper,
which contains a description of the steady-state pseudo 2D model. The
extreme fill website and Github repository contain the necessary
documentation and code to run the FiPy model of extreme fill as well
as generate the data to completely reproduce the images in the paper.
