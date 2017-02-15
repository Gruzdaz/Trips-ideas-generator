"""Bomztrip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from search.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^trips$', trips),
    url(r'^affiliates$', affiliates),
    url(r'^contacts$', contacts),
    url(r'^random_trip/$', random_trip, name='random_trip'),
    url(r'^like/$', like , name='like'),
    url(r'^(?P<title>[\w.@+-]+)/$',
                       single_trip,
                       name='single_trip'),
    url(
        r'search-autocomplete/$',
        SearchAutocomplete.as_view(),
        name='search-autocomplete',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
