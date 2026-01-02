from django.urls import path
from .views import *
app_name='plant'
urlpatterns = [

    path('index',plant_index,name='index'),
<<<<<<< HEAD
    path('<int:id>/delete',plant_delete,name='delete'),
    path('<int:id>/detail',plant_detail,name='detail'),
    path('<int:id>/update',plant_update,name='update'),
    path('create',plant_create,name='create'),
    path('<int:id>/carelog/create/',carelog_create,name='carelog_create'),
=======
    path('delete',plant_delete,name='delete'),
    path('<int:id>/',plant_detail,name='detail'),
    path('update',plant_update,name='update'),
    path('create',plant_create,name='create'),

>>>>>>> 7160f4d21e2332bebb61782cb3b7a70d4d89e490
]
