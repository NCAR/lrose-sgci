from django.conf.urls import url, include

from . import views

# Note that app_name specifies the namespace for your app's urls and should be changed to something appropriate for your app

app_name = 'custom_app'
urlpatterns = [
    url(r'^hello/', views.hello_world, name="home"),
]
