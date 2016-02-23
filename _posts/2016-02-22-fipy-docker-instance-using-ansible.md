---
layout: post
title: "FiPy Docker Instance using Ansible"
category: posts
---

I created a [repository](https://github.com/wd15/fipy-dockerize) that
uses both Ansible and Docker to generate a Docker instance of
[FiPy](https://github.com/usnistgov/fipy). The main benefit of using
Ansible in this situation is that it makes the developer generate a
very clearly formatted file for the installation procedure. See,
[the Ansible YAML file](https://github.com/wd15/fipy-dockerize/blob/master/setup.yml). This
file could be reused outside of a Docker instance for installation as
well. A
[`setup.bash`](https://github.com/wd15/fipy-dockerize/blob/master/setup.bash)
is still required to bootstrap the Ansible installation in the event
that Ansible isn't installed.  The installation procedure that's in
the Ansible YAML file could either be buried in the
[`setup.bash`](https://github.com/wd15/fipy-dockerize/blob/master/setup.bash)
or the
[`Dockerfile`](https://github.com/wd15/fipy-dockerize/blob/master/Dockerfile). Ansible
seems to do a nice job of creating a clean set of declarative
statements for the installation procedure.
