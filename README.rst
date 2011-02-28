===========
Django Fail
===========

**Django Fail** provides tools for testing your site under less-than-ideal
conditions.

When working locally, response times are near instant, and there is no entropy
introduced by network hardware (e.g. proxies or load balancers) that may, for
some reason or other, fail.

**Django Fail** helps you test what happens when some parts of your site don't
load or load slowly. This can be particularly helpful for responses used in
Ajax-powered applications.


``@fail(status=500, content='', mimetype='text/html')``
=======================================================

The ``@fail()`` decorator makes a view return some kind of failure response,
instead of a real response.

For the arguments, ``status`` is the status code, normally ``500``, ``content``
is any content to return, normally ``''``, and ``mimetype`` is the mimetype of
the response, normally ``text/html``.

The ``@fail()`` decorator can be globally disabled by adding ``FAIL_ON =
False`` to ``settings.py``.


``@slow(delay=2)``
==================

The ``@slow()`` decorator makes a response wait a while before returning. The
delay is in seconds and defaults to ``2``.

The ``@slow()`` decorator can be globally disabled by adding ``SLOW_ON =
False`` to settings.py.
