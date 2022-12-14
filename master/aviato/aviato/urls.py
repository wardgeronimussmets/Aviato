"""aviato URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("karting/",include("karting_grapher.urls")),
    path("raspman/",include("raspman.urls")),
    path("notifier/",include("notifier.urls")),
    path("ibood/",include("iBOOD.urls")),

]

#start all the jobs that need to be running in the background
from . import jobs
jobs.start_scheduler()

# #### code that prints the whole stack together with the print statements
# import sys
# import traceback

# class TracePrints(object):
#   def __init__(self):    
#     self.stdout = sys.stdout
#   def write(self, s):
#     self.stdout.write("Writing %r\n" % s)
#     traceback.print_stack(file=self.stdout)

# sys.stdout = TracePrints()


