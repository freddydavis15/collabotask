from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'add', views.fun, name="fun"),
    url(r'^(?P<param>.*/)', views.joke, name="joke"),

]

