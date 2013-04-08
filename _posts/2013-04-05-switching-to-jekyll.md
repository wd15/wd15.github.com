---
layout: post
title: "Switching to Jekyll"
description: ""
category: 
tags: []
---
{% include JB/setup %}

I finally decided to move away from my old [Trac Blog][TracBlog] at
[Matforge](http://matforge.org). [Jekyll Bootstrap][JekyllBootstrap]
seems like a good alternative as most of my research has moved to
Github repositories in the last year. The main benefit of the
[Trac Blog][TracBlog] was the close integration with the Subversion
repository, which I now of course no longer use.  The overriding
benefit of using Jekyll is having the posts stored as plain markup in
a local Git repository independently from either the blogging tool or
the blog design. Also, using Jekyll presents a very low barrier to
switching between blogging tools. There is also the added benefit of
testing locally before publishing.

#### Resources

The [Jekyll Bootstrap site][JekyllBootstrap] has mostly everything
needed to get started. To add in maths support I found
[Dason Kurkiewicz's site](http://dasonk.github.com/blog/2012/10/09/Using-Jekyll-and-Mathjax/)
which had very clear instructions.  So, using the Mathjax plugin,

{% highlight latex %}
\frac{\partial \phi}{\partial t} = -\phi^2 + a^2
{% endhighlight %}

renders as

$$\frac{\partial \phi}{\partial t} = -\phi^2 + a^2$$

Code seems to look good:

{% highlight python %}
for i in range(10):
    print i
{% endhighlight %}

I chose to use
[the-minimum](http://themes.jekyllbootstrap.com/preview/the-minimum/)
Jekyll Bootstrap theme and tweaked only a very few
things. Unfortunately, I don't know nearly enough about the way Jekyll
and css work to make the changes that I want at the moment. Hopefully,
the site will improve over time.

Other resources:

  * [A list of nice Jekyll Bootstrap sites.](https://github.com/mojombo/jekyll/wiki/Sites)
  
[TracBlog]: http://matforge.org/wd15/blog
[JekyllBootstrap]: http://jekyllbootstrap.com/
