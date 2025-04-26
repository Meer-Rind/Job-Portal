from django import forms
from .models import Job, JobCategory
from .constants import JOB_TYPE_CHOICES  # Import from constants

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'job_type', 'category', 'salary', 'deadline', 'requirements']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5}),
            'requirements': forms.Textarea(attrs={'rows': 5}),
        }

class JobCategoryForm(forms.ModelForm):
    class Meta:
        model = JobCategory
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class JobSearchForm(forms.Form):
    title = forms.CharField(required=False)
    location = forms.CharField(required=False)
    job_type = forms.ChoiceField(choices=[('', 'All Types')] + JOB_TYPE_CHOICES, required=False)
    category = forms.ModelChoiceField(queryset=JobCategory.objects.all(), required=False)