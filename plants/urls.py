from django.urls import path
from .views import *
app_name='plant'
urlpatterns = [

    path('index',plant_index,name='index'),
    path('<int:id>/delete',plant_delete,name='delete'),
    path('<int:id>/detail',plant_detail,name='detail'),
    path('<int:id>/update',plant_update,name='update'),
    path('create',plant_create,name='create'),
    path('<int:id>/carelog/create/',carelog_create,name='carelog_create'),
]
