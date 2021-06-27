from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('sports/', views.sports),
    path('business/', views.business),
    path('scitech/', views.scitech),

]

