from django.urls import path, re_path as url
# from django.conf.urls import url
# from rest_framework import routers
# from . import views
from rest_framework.routers import DefaultRouter
from todo.views import TodoViewSet, UserAuth, UserRegister

# creating instance of router
router = DefaultRouter()
# registering router
router.register(r'todo', TodoViewSet, basename='todo')

urlpatterns = [
    url(r'^login/$', UserAuth.as_view()),
    url(r'^register/$', UserRegister.as_view()),
]


urlpatterns = urlpatterns + router.urls

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('dummy', views.dummy, name='dummy'),
#     url(r'^(?P<pk>\d+)/$', views.index, name='test_regex'),
# ]
