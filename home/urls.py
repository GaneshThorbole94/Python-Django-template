from django.urls import path

from . import views

urlpatterns = [
     path('',views.home),
     path('contacts/',views.contacts),
     path('trainings/',views.trainings),
     path('shortcodes/',views.shortcodes),
     path('shows/',views.shows),
     path('classes/',views.classes),
   ]