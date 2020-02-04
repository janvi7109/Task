from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^/$', views.login, name="login"),
    url(r'^registration.html', views.register, name="registration"),
]