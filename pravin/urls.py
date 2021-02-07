from  django.urls import path
from . import views

urlpatterns = [
  path('',views.priyank,name='pryank'),
  path('add',views.add,name='add')
]
