from django.contrib import admin
from django.urls import path,include
from .views import marsview
 
urlpatterns=[
  path('admin/',admin.site.urls),
  path("",marsview),

 ]