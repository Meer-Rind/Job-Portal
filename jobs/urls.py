from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
    path('jobs/post/', views.post_job, name='post_job'),
    path('jobs/<int:pk>/update/', views.update_job, name='update_job'),
    path('jobs/<int:pk>/delete/', views.delete_job, name='delete_job'),
    path('jobs/manage/', views.manage_jobs, name='manage_jobs'),
    path('categories/manage/', views.manage_categories, name='manage_categories'),
    path('categories/<int:pk>/delete/', views.delete_category, name='delete_category'),
]