from django.urls import path 
from .views import base , logout_view

urlpatterns = [
    path('', base), 
    path('logout/', logout_view, name='logout_view')
]