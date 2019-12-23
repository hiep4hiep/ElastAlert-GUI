"""elastalert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from rule import views

urlpatterns = [
    path('',views.home, name='home'),
    path('admin/', admin.site.urls),
    url(r'^create/$', views.create_rule, name='create_rule'),
    url(r'^rules/(?P<pk>\d+)/$', views.view_rule, name='view_rule'),
    url(r'^rules/delete/(?P<pk>\d+)/$', views.delete_rule, name='delete_rule'),
    url(r'^rules/run/(?P<pk>\d+)/$', views.run_rule, name = 'run_rule'),
    #url(r'^rules/(?P<pk>[\w.@+-]+)/$', views.view_rule, name='view_rule'),
]
admin.site.site_header = "InnoBox Admin portal"
admin.site.site_title = "InnoBox Admin Portal"
admin.site.index_title = "User and Rule management"
