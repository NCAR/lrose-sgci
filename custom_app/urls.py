from django.urls import path

from . import views

# Note that app_name specifies the namespace for your app's urls and should be changed to something appropriate for your app

app_name = 'custom_app'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('hello/', views.hello_world, name='hello_world'),
    path('custom_nav/', views.custom_nav, name='custom_nav'),
]
