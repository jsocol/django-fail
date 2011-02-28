from functools import wraps
import time

from django.conf import settings
from django.http import HttpResponse


def fail(status=500, content='', mimetype='text/html'):
    """Return some kind of failure instead of the real response."""
    def decorator(view):
        @wraps(view)
        def _wrapped(request, *args, **kw):
            on = getattr(settings, 'FAIL_ON', True)
            if on:
                return HttpResponse(content, status=status, mimetype=mimetype)
            return view(request, *args, **kw)
        return _wrapped
    return decorator


def slow(delay=2):
    def decorator(view):
        @wraps(view)
        def _wrapped(request, *args, **kw):
            on = getattr(settings, 'SLOW_ON', True)
            if on:
                time.sleep(delay)
            return view(request, *args, **kw)
        return _wrapped
    return decorator
