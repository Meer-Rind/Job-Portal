from django.db import models
from accounts.models import JobSeeker
from jobs.models import Job
from django.utils import timezone

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    application_date = models.DateTimeField(default=timezone.now)
    cover_letter = models.TextField()
    status = models.CharField(max_length=20, default='Pending', choices=[
        ('Pending', 'Pending'),
        ('Reviewed', 'Reviewed'),
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
    ])
    
    def __str__(self):
        return f"{self.applicant.user.username} - {self.job.title}"
    
    class Meta:
        unique_together = ('job', 'applicant')
        ordering = ['-application_date']