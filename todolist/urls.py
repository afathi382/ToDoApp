from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home , name='home'),
    path('about/', views.about , name='about'),
    path('delete/<list_id>', views.delete , name='delete'),  
    path('cross_off/<list_id>', views.cross_off , name='cross_off'),
    path('edit/<list_id>', views.edit , name='edit'),     
] 

