from unicodedata import name
from django.urls import path
from mainApp import views


urlpatterns = [
    path('',views.Home,),
    path('delete/<int:id>/',views.Delete_pic,name='delete')
] 