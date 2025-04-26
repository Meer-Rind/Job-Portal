from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:pk>/', views.apply_job, name='apply_job'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('application/<int:pk>/', views.view_application, name='view_application'),
    path('application/<int:pk>/<str:status>/', views.update_application_status, name='update_application_status'),
    path('job/<int:job_pk>/applications/', views.job_applications, name='job_applications'),
]