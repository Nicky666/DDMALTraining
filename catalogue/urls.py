"""catalogue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from catalogue.views.source import SourceListView, SourceDetailView
from catalogue.views.archive import ArchiveListView, ArchiveDetailView
from catalogue.views.composition import CompositionListView, CompositionDetailView
from catalogue.views.composer import ComposerListView, ComposerDetailView
from catalogue.views.composed import ComposedListView, ComposedDetailView
from catalogue.views.search import SearchListView


urlpatterns = [
    url(r'^sources/$', SourceListView.as_view(), name="source-list"),
    url(r'^sources/(?P<pk>[0-9]+)/$', SourceDetailView.as_view(), name="source-detail"),

    url(r'^archives/$', ArchiveListView.as_view(), name="archive-list"),
    url(r'^archives/(?P<pk>[0-9]+)/$', ArchiveDetailView.as_view(), name="archive-detail"),

    url(r'^composition/$', CompositionListView.as_view(), name="composition-list"),
    url(r'^compositions/(?P<pk>[0-9]+)/$', CompositionDetailView.as_view(), name="composition-detail"),

    url(r'^composers/$', ComposerListView.as_view(), name="composer-list"),
    url(r'^composers/(?P<pk>[0-9]+)/$', ComposerDetailView.as_view(), name="composer-detail"),

    url(r'^composeds/$', ComposedListView.as_view(), name="composed-list"),
    url(r'^composeds/(?P<pk>[0-9]+)/$', ComposedDetailView.as_view(), name="composed-detail"),

    url(r'^search/?$', SearchListView.as_view(), name="search-list"),

    url(r'^admin/', admin.site.urls),
]
