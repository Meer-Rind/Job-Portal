from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Job, JobCategory
from .forms import JobForm, JobCategoryForm, JobSearchForm
from accounts.models import Employer
from applications.models import Application

def home(request):
    jobs = Job.objects.filter(is_active=True).order_by('-posted_date')[:6]
    categories = JobCategory.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs, 'categories': categories})

def job_list(request):
    form = JobSearchForm(request.GET or None)
    jobs = Job.objects.filter(is_active=True).order_by('-posted_date')
    
    if form.is_valid():
        title = form.cleaned_data.get('title')
        location = form.cleaned_data.get('location')
        job_type = form.cleaned_data.get('job_type')
        category = form.cleaned_data.get('category')
        
        if title:
            jobs = jobs.filter(Q(title__icontains=title) | Q(description__icontains=title))
        if location:
            jobs = jobs.filter(location__icontains=location)
        if job_type:
            jobs = jobs.filter(job_type=job_type)
        if category:
            jobs = jobs.filter(category=category)
    
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'form': form})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    has_applied = False
    
    if request.user.is_authenticated and request.user.is_jobseeker:
        has_applied = Application.objects.filter(job=job, applicant=request.user.jobseeker).exists()
    
    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'has_applied': has_applied
    })

@login_required
def post_job(request):
    if not request.user.is_employer:
        messages.warning(request, 'Only employers can post jobs!')
        return redirect('home')
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user.employer
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm()
    
    return render(request, 'jobs/post_job.html', {'form': form})

@login_required
def update_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    if not request.user.is_employer or job.employer != request.user.employer:
        messages.warning(request, 'You can only update your own jobs!')
        return redirect('home')
    
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm(instance=job)
    
    return render(request, 'jobs/update_job.html', {'form': form, 'job': job})

@login_required
def delete_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    if not request.user.is_employer or job.employer != request.user.employer:
        messages.warning(request, 'You can only delete your own jobs!')
        return redirect('home')
    
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')
        return redirect('home')
    
    return render(request, 'jobs/delete_job.html', {'job': job})

@login_required
def manage_jobs(request):
    if not request.user.is_employer:
        messages.warning(request, 'Only employers can manage jobs!')
        return redirect('home')
    
    # Ensure the employer profile exists
    employer, created = Employer.objects.get_or_create(user=request.user)
    
    jobs = Job.objects.filter(employer=employer).order_by('-posted_date')
    return render(request, 'jobs/manage_jobs.html', {'jobs': jobs})
@login_required
def manage_categories(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Only admin can manage categories!')
        return redirect('home')
    
    categories = JobCategory.objects.all()
    
    if request.method == 'POST':
        form = JobCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('manage_categories')
    else:
        form = JobCategoryForm()
    
    return render(request, 'jobs/manage_categories.html', {
        'categories': categories,
        'form': form
    })

@login_required
def delete_category(request, pk):
    if not request.user.is_superuser:
        messages.warning(request, 'Only admin can delete categories!')
        return redirect('home')
    
    category = get_object_or_404(JobCategory, pk=pk)
    
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully!')
        return redirect('manage_categories')
    
    return render(request, 'jobs/delete_category.html', {'category': category})