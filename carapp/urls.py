
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.apiOverview, name='apiOverview'),

    path('model-list/', views.ShowAll, name='ShowAll'),
    path('model-detail/<int:pk>/', views.ViewModel, name='ViewModel'),
    path('model-create/', views.CreateModel, name='CreateModel'),
    path('model-update/<int:pk>/', views.updateModel, name='updateModel'),
    path('model-delete/<int:pk>/', views.deleteModel, name='deleteModel'),


]

