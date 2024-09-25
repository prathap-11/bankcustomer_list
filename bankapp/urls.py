from django.urls import path
from . import views

urlpatterns = [
    path('',views.read_,name='index'),
    path('add/',views.add_),
    path('upd/<int:ik>/',views.update_),
    path('del/<ik>',views.delete_)
]