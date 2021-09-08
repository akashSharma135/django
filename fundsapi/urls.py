from django.urls import path
from .views import AMCView, NavView, SchemeView, NavDetailView

urlpatterns = [
    path('amc', AMCView.as_view()),
    path('scheme', SchemeView.as_view()),
    path('nav/', NavView.as_view()),
    path('nav/<int:id>/', NavDetailView.as_view()),
]