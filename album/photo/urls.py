from django.urls import path
from photo.views import (
        home,
        upload,
        oss_home,
        fetch_photos,
    )
from django.views.generic import TemplateView
from photo.views import home, upload, oss_home
# App名称
# 用于Django幕后的url查询
app_name = 'photo'
# url列表
urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload, name='upload'),
    path(
        'endless-home/',
        TemplateView.as_view(template_name='photo/endless_list.html'),
        name='endless_home'
    ),
    path('fetch/', fetch_photos, name='fetch'),
    path('oss-home/', oss_home, name='oss_home'),
]