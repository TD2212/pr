from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name='home'),
    path('list/', views.student_list, name='list'),
    path('add/',views.st_add,name='add'),
    path('delete/<int:id>/', views.st_delete, name='delete'),
    path('update/<int:id>/', views.st_update, name='update'),
]