from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'Main page'),
    path('input/', views.input, name = 'Input page'),
    path('input/table_page/', views.table_page, name= "Table page"),
    path('<int:pk>', views.InputUpdateView.as_view(), name = "update_page"),
]