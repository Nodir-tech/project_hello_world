from django.urls import path
from .views import HomePageView,AboutPage,Base

urlpatterns = [
    path('home/',HomePageView.as_view(),name='home'),
    path('about/',AboutPage.as_view(),name='about'),
    path('',Base.as_view(),name='base'),
]