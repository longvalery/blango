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
from django.urls import path
# other imports
import blog.views
from django.conf import settings
import logging



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
              ]
