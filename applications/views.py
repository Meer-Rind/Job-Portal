from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jobs.models import Job
from .models import Application
from .forms import ApplicationForm
from accounts.models import JobSeeker

@login_required
def apply_job(request, pk):
    if not request.user.is_jobseeker:
        messages.warning(request, 'Only job seekers can apply for jobs!')
        return redirect('home')
    
    job = get_object_or_404(Job, pk=pk)
    jobseeker = request.user.jobseeker
    
    if Application.objects.filter(job=job, applicant=jobseeker).exists():
        messages.warning(request, 'You have already applied for this job!')
        return redirect('job_detail', pk=job.pk)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = jobseeker
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = ApplicationForm()
    
    return render(request, 'applications/apply_job.html', {
        'form': form,
        'job': job
    })

@login_required
def my_applications(request):
    if not request.user.is_jobseeker:
        messages.warning(request, 'Only job seekers can view applications!')
        return redirect('home')
    
    applications = Application.objects.filter(applicant=request.user.jobseeker).order_by('-application_date')
    return render(request, 'applications/my_applications.html', {'applications': applications})

@login_required
def view_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    
    if not request.user.is_employer or application.job.employer != request.user.employer:
        if not (request.user.is_jobseeker and application.applicant == request.user.jobseeker):
            messages.warning(request, 'You are not authorized to view this application!')
            return redirect('home')
    
    return render(request, 'applications/view_application.html', {'application': application})

@login_required
def update_application_status(request, pk, status):
    if not request.user.is_employer:
        messages.warning(request, 'Only employers can update application status!')
        return redirect('home')
    
    application = get_object_or_404(Application, pk=pk)
    
    if application.job.employer != request.user.employer:
        messages.warning(request, 'You can only update applications for your jobs!')
        return redirect('home')
    
    if status not in ['Pending', 'Reviewed', 'Rejected', 'Accepted']:
        messages.warning(request, 'Invalid status!')
        return redirect('view_application', pk=application.pk)
    
    application.status = status
    application.save()
    messages.success(request, f'Application status updated to {status}!')
    return redirect('view_application', pk=application.pk)

@login_required
def job_applications(request, job_pk):
    if not request.user.is_employer:
        messages.warning(request, 'Only employers can view job applications!')
        return redirect('home')
    
    job = get_object_or_404(Job, pk=job_pk)
    
    if job.employer != request.user.employer:
        messages.warning(request, 'You can only view applications for your jobs!')
        return redirect('home')
    
    applications = Application.objects.filter(job=job).order_by('-application_date')
    return render(request, 'applications/job_applications.html', {
        'job': job,
        'applications': applications
    })