from django.contrib import admin
from django.urls import path, re_path

from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.posts),
    path('<int:post_id>/',views.post_detail),
    re_path(r'^archive/(?P<year>)[0-9]{4}/$',views.post_archive),
    path('post/get_post/',views.get_post_handler)
]

handler404 = views.page404