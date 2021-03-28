from  django.urls import path
from . import views

urlpatterns = [

  path('',views.priyank),
  path('add',views.add),
  path('hello',views.hello)

]
