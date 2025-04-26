from django.db import models
from accounts.models import Employer
from django.utils import timezone
from .constants import JOB_TYPE_CHOICES  # Import from constants

class JobCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True, blank=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    posted_date = models.DateTimeField(default=timezone.now)
    deadline = models.DateField()
    requirements = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-posted_date']