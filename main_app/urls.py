from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('models/', views.Model_List.as_view(), name="model_list"),
    path('models/new/', views.Model_Create.as_view(), name="model_create"),
    path('models/<int:pk>/', views.Model_Detail.as_view(), name="model_detail"),
    path('models/<int:pk>/update', views.Model_Update.as_view(), name="model_update"),
    path('models/<int:pk>/delete', views.Model_Delete.as_view(), name="model_delete"),
    path('user/<username>/', views.profile, name='profile'),
    path('paint/', views.paint_list, name="paint_list"),
    path('paint/new/', views.Paint_Create.as_view(), name="paint_create"),
    path('paint/<int:pk>/', views.paint_detail, name="paint_detail"),
    path('paint/<int:pk>/update', views.Paint_Update.as_view(), name="paint_update"),
    path('paint/<int:pk>/delete', views.Paint_Delete.as_view(), name="paint_delete"),
]