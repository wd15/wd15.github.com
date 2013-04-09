---
layout: post
title: "Configuring Sumatra for Postgres"
description: ""
category: 
tags: []
---
{% include JB/setup %}

For the last few months I've been using [Sumatra][SMT] to log the
provenance data for simulations. It's a really promising tool, and I've
been hacking on it from time to time as I proceed with real
research. Sumatra even has a web interface driven by Django and uses
SQLite as the default back end database.

One of the issues with SQLite is concurrency. This issue manifests
itself with Sumatra when dozens of jobs are launched simultaneously
with each job having a similar life time. In this event most of the
jobs are not recorded and the unrecorded jobs will sign off with the
dreaded `django.db.utils.DatabaseError: database is locked`. For
further discussion on this issue the
[Sumatra mailing list thread on this topic](https://groups.google.com/forum/?fromgroups=#!topic/sumatra-users/-9Gci0thFLo).

### Quick and Dirty Solution

In the short term, I decided to use a quick and dirty solution to work
around this issue using file locks. I couldn't face learning to
configure Postgres, so the file lock solution allowed me to proceed
with my work without having to learn the ins and outs of configuring
Django and Postgres.

The solution required creating a decorator class
[available at Github](https://github.com/wd15/sumatra/blob/8b39d73b3cf85dbb8f2ada44a6914a27dff718df/src/smtdecorator.py)
that encapsulated the Python function to be logged. The two Sumatra
command that need to be protected from concurrency issues are
`project.add_record` and `project.save`. Here the `with` statement is
used to set and release the lock:

{% highlight python %}
with SMTLock(project):
    project.add_record(record)
    project.save()
{% endhighlight %}

where `SMTLock` is defined as

{% highlight python %}
class SMTLock:
    def __init__(self, project):
        self.lock = lockfile.FileLock(
            os.path.split(_get_project_file(project.path))[0])

    def __enter__(self):
        self.lock.acquire()

    def __exit__(self, type, value, tb):
        self.lock.release()
{% endhighlight %}

The above class requires the
[lockfile module](https://pypi.python.org/pypi/lockfile). The file
locking mechanism worked well enough and might be a solution for some
that want to maintain a lightweight database solution with
Sumatra. However, it does require making changes to the script or
program for which the provenance data is being logged. This goes
against the grain of the "don't change the existing workflow" approach
of Sumatra.

### Postgres

Given that the above solution is unsatisfactory, the best alternative
seems to be to use Postgres. To install Postgres on Ubuntu use:

{% highlight bash %}
$ sudo apt-get install postgresql
{% endhighlight %}

Set the Postgres 
http://blog.iiilx.com/programming/how-to-install-postgres-on-ubuntu-for-django/



[SMT]: http://neuralensemble.org/sumatra/


