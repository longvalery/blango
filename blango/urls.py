"""blango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
# from django.contrib.staticfiles import views
# other imports
import blog.views
from django.conf import settings
import logging
from django.core.cache import caches

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .settings import DEBUG

# cache is the equivalent of caches["default"]/our default_cache variable
default_cache = caches["default"]
# post_pk = 1
# p = Post.objects.get(pk=1)
# cache.set(f"post_{post_pk}", p, 30)
# Notice we’re using the Post object’s primary key as part of its cache key, so we can be sure the cache key is unique.
# Then, let’s get Post back out of the cache (although if it’s been more than 30 seconds since you’ve set it, you’ll need to put it back into the cache otherwise this won’t work)
# p1 = cache.get(f"post_{post_pk}")
# print(p == p1) # Out: True
# Now wait 30 seconds, and try to retrieve the Post object from the cache again.
# print(cache.get(f"post_{post_pk}")) # Out: None

# If we don’t want to wait for the timeout to elapse, then we can just use the delete() method to remove an item from the cache. For example, if a Post was updated we could remove its old, cached version. delete() takes two arguments, the key to delete and the cache key version, which is optional. It will return True if the value existed in the cache prior to deletion, or False if it did not.
# cache.delete(f"post_{post_pk}")

# If we try to fetch a value that doesn’t exist in the cache, we’ll get back None, so how can we differentiate between a value that’s not in the cache and a stored None value? The trick is to pass a sentinel object as the default to get(). If you get the same sentinel back, you know the key wasn’t set. If you get None, you’ll know the value None was set.
# sentinel = object()
# cache.set("current_user", None, 30)
# u = cache.get("current_user", sentinel)
# print(u is None)     #Out: True
# print(u is sentinel) #Out: False


logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('----start messages-----') 
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")


try:
    answer = 9 / 0
    print(f"The answer is: {answer}")
    raise_exception()
except ZeroDivisionError:
    logger.exception("!!!! A divide by zero exception occured")

username="rva"
email="domino-sender@mail.ru"
logger.log(logging.DEBUG, "Created user %s with email %s", username, email)

logger.debug('----stop messages-----') 

# For performance reasons, pre-interpolated strings shouldn’t be passed to the logging function.
# For example, these two lines would produce the same log output:
##logger.debug("Created user %s with email %s" % (username, email))
##logger.debug("Created user %s with email %s", username, email)
# However, in the first usage, the string is formatted and then sent to the logging function. If the logging level of the logger is not DEBUG then the message will be discarded.
# In the second call, if the logger level is not DEBUG then the message is discarded before it’s interpolated, thus preventing the (admittedly small) overhead of this operation.

print(f"Time zone: {settings.TIME_ZONE}")

urlpatterns = [
    path('admin/', admin.site.urls),
    # other patterns
    path("", blog.views.index) ,
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
    path("ip/", blog.views.get_ip),
              ]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if DEBUG:
  # print("DEBUG:",DEBUG)
  # print("STATIC_ROOT:",settings.STATIC_ROOT)
  # print("STATIC_URL:",settings.STATIC_URL)
  #print("re_path(r'^static/(?P<path>.*)$', serve): ",re_path(r'^static/(?P<path>.*)$', serve))
  urlpatterns += staticfiles_urlpatterns() 
  # urlpatterns += [
  #      re_path(r'^static/(?P<path>.*)$', serve, {
  #          'document_root': settings.STATIC_ROOT, })     
  #             ] 

  print("staticfiles_urlpatterns() :",staticfiles_urlpatterns())              
## urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  print("static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) :"
     ,static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
  print("static :"
     ,static("/--/", document_root="/+++/"))     
  import debug_toolbar
  urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
               ]

print(urlpatterns)


