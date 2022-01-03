"""design_construction URL Configuration

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
from django.urls import path,include,re_path
from django.conf import settings
#from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    #path('jet/', include('jet.urls', 'jet')),
    #path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('department/',include('department.urls')),
    path('documents/',include('documents.urls')),
    path('insight/',include('insight.urls')),
    path('project_tracker/',include('project_tracker.urls')),
    path('payment_tracker/',include('payment_tracker.urls')),
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),

]