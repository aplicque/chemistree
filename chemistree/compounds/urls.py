from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('compounds', views.compounds, name='compounds'),
    path('elements', views.elements, name='elements'),
    path('compounds/inspect/<compid>', views.compinspect, name='compinspect'),
    path('elements/inspect/<elemid>', views.eleminspect, name='eleminspect')





]