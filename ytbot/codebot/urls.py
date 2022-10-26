from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.main, name='home'),
    path('about', views.about, name='about'),
    path('recs/deep', views.goDeep, name='deepfake')
]