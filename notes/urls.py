from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('list/', views.note_list, name='list'),
    path('create/', views.note_create, name='create'),
    path('detail/<int:pk>/', views.note_detail, name='detail'),
    path('delete/<int:pk>/', views.note_delete, name='delete'),
    path('update/<int:pk>/', views.note_update, name='update'),
]
