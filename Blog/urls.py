"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from myblog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list_view),
    path('<year>/<month>/<day>/<post>',views.post_detail_view,name='post_detail'),
    path('<int:id>/share',views.mail_send_view),
    path('list/',views.listview),
]


# from django.urls import re_path as url
# from django.contrib import admin
# from myblog import views

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', views.post_list_view),
#     url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view,name='post_detail'),
#     url('r^(?P<id>\d+)/share/$',views.mail_send_view),
#     ]