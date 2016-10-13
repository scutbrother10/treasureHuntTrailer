"""treasureHuntTrailer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from search.views import search,search_form
from trailer.views import video_list_view, video_detail_view, check_product_info_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search-form/$', search_form),
    url(r'^search/$', search),
    url(r'^video_index/$',video_list_view),
    url(r'^video_index/(?P<video_id>\d{0,7})/$', video_detail_view),
    url(r'^check_product_info/$', check_product_info_view),
]