from django.urls import path
app_name='homepage'
from . import views
from django.conf.urls import include
urlpatterns = [
    path('',views.index,name='index'),
    path('soon/',views.coming_soon,name='soon'),
    path('register/',views.register_form,name='register'),
]
