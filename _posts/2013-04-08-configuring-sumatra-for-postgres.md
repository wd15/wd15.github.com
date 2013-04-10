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
further discussion of this issue see the
[Sumatra mailing list thread on this topic](https://groups.google.com/forum/?fromgroups=#!topic/sumatra-users/-9Gci0thFLo).

### Quick and Dirty Solution

In the short term, I decided to use a quick and dirty solution to work
around this issue using file locks. I couldn't face learning to
configure Postgres as I have little to no experience with databases.
The file lock solution allowed me to proceed with my work without
having to learn the ins and outs of configuring Django and Postgres.

The solution required creating a decorator class
[available at Github](https://github.com/wd15/sumatra/blob/8b39d73b3cf85dbb8f2ada44a6914a27dff718df/src/smtdecorator.py)
that encapsulated the Python function to be logged. The two Sumatra
commands that need to be protected from concurrency issues are
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
locking mechanism worked well enough and might be a solution for those
that wish to maintain a lightweight database solution with
Sumatra. However, it does require making changes to the script or
program for which the provenance data is being logged. This goes
against the grain of the "don't change the existing workflow" approach
of Sumatra.

### Postgres

Given that the above solution is unsatisfactory, another alternative
is to use a database that properly handles concurrency. To install
Postgres on Ubuntu use

{% highlight bash %}
$ sudo apt-get install postgresql
$ sudo apt-get install python-psycopg2
{% endhighlight %}

and then use

{% highlight bash %}
$ sudo passwd postgres
{% endhighlight %}

to set the password. Then create a Sumatra user for Postgres using

{% highlight bash %}
$ sudo -u postgres createuser -P sumatra_user
{% endhighlight %}

To create a database do

{% highlight bash %}
$ su postgres
postgres$ psql template1
{% endhighlight %}
{% highlight psql %}
template1=# CREATE DATABASE sumatra_db OWNER sumatra_user ENCODING 'UTF8';
{% endhighlight %}

Exit the Postgres shell prompts and edit
`/etc/postgresql/9.1/main/pg_hba.conf` by adding

{% highlight python %}
local      sumatra_db   sumatra_user   trust
{% endhighlight %}

and relaunch Postgres

{% highlight bash %}
$ sudo /etc/init.d/postgresql restart
{% endhighlight %}

If Sumatra gives errors during configuration and the database has the
wrong field sizes then you'll need to repeat the process above to
create a new database. You can delete the old database with

{% highlight psql %}
template1=# DROP DATABASE sumatra_db
{% endhighlight %}

These instructions were snatched from
[iiilx's blog](http://blog.iiilx.com/programming/how-to-install-postgres-on-ubuntu-for-django/).
Now that Postgres is working we can move on to setting up Sumatra.

### Configuring Sumatra

Edit the Django database configuration in
`src/recordstore/django_store/__init__.py` to swap SQLite for
Postgres.

{% highlight diff %}
             self._settings['DATABASES'][label] = {
-                'ENGINE': 'django.db.backends.sqlite3',
-                'NAME': os.path.abspath(db_file)
+                'ENGINE':
+                'django.db.backends.postgresql_psycopg2',
+                'NAME': 'sumatra_db',
+                'USER': 'sumatra_user',
+                'PASSWORD': 'password',
+                'HOST': 'localhost'
             }
{% endhighlight %}

Ideally this would be the only change required, however, there is an
issue with the field sizes in Sumatra. Using Sumatra with the above
configuration will result in Postgres errors of the type
`DatabaseError: value too long for type character varying(100)`.  This
error is caused because the field sizes have never been checked with
anything but SQLite and SQLite has no size limits in the way that
Postgres does (see this
[stackoverflow thread](http://stackoverflow.com/questions/13736059/databaseerror-at-post-113-value-too-long-for-type-character-varying10)
for more details). Anyway, fixing the field size problem simply
requires making a number of changes like this

{% highlight diff %}
-    type = models.CharField(max_length=20)
+    type = models.CharField(max_length=100)
{% endhighlight %}

in `src/recordstore/django_store/models.py`. There are about 10 of
these altogether (see the
[full changeset](https://github.com/wd15/sumatra/commit/0bcafc468c5fe4b93e4f230ad37aca00811ef6ff)
for a complete list). The above instructions are valid as of commit
[d65bb4fa1f83](https://neuralensemble.org/hg/sumatra/rev/d65bb4fa1f83).

### Testing Sumatra for Concurrency

The following is a test to see that it works. Set up a trivial `script.py`,

{% highlight python linenos %}
import time
import sys

param_file = sys.argv[1]
f = open(param_file, 'r')
exec f.read()

print 'waiting for ' + str(wait) + '(s)'
time.sleep(wait)
print 'finished'
{% endhighlight %}

and a parameter file (`default.param`) with

{% highlight python linenos %}
wait=3
{% endhighlight %}

Set up a Git repository.

{% highlight bash %}
$ git init
$ git add script.py default.param
$ git ci -m "First commit."
{% endhighlight %}

Set up a Sumatra repository.

{% highlight bash %}
$ smt init postgres_test
$ smt configure --executable=python --main=script.py
$ smt configure --addlabel=cmdline
$ smt configure -g uuid
$ smt configure -c store-diff
$ smt run default.param wait=5
{% endhighlight %}

Check the repository with `smtweb`. There should be one record. Now to
test the concurrency use

{% highlight bash %}
$ for i in $(seq 100); do smt run default.param wait=3 &> /dev/null & done
{% endhighlight %}

Check the repository. 101 records. No concurrency issues!

### What next?

In the near future I hope to submit a patch for this and include some
kind of command line configuration for Sumatra to allow easy set
up. Something like this

{% highlight bash %}
$ smt configure --database=postgres --name=sumatra_db --user=sumatra_user --password=password
{% endhighlight %}

[SMT]: http://neuralensemble.org/sumatra/


