from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    JobSeekerSignUpForm, 
    EmployerSignUpForm, 
    UserUpdateForm, 
    JobSeekerUpdateForm, 
    EmployerUpdateForm
)
from .models import User, JobSeeker, Employer

def register_jobseeker(request):
    if request.method == 'POST':
        form = JobSeekerSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = JobSeekerSignUpForm()
    return render(request, 'accounts/register_jobseeker.html', {'form': form})

def register_employer(request):
    if request.method == 'POST':
        form = EmployerSignUpForm(request.POST, request.FILES)  # Make sure to include request.FILES
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = EmployerSignUpForm()
    return render(request, 'accounts/register_employer.html', {'form': form})

def register(request):
    return render(request, 'accounts/register.html')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        
        if request.user.is_jobseeker:
            profile_form = JobSeekerUpdateForm(request.POST, instance=request.user.jobseeker)
        elif request.user.is_employer:
            profile_form = EmployerUpdateForm(request.POST, request.FILES, instance=request.user.employer)
        else:
            profile_form = None
        
        if user_form.is_valid() and (profile_form is None or profile_form.is_valid()):
            user_form.save()
            if profile_form:
                profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        if request.user.is_jobseeker:
            profile_form = JobSeekerUpdateForm(instance=request.user.jobseeker)
        elif request.user.is_employer:
            profile_form = EmployerUpdateForm(instance=request.user.employer)
        else:
            profile_form = None
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'accounts/profile.html', context)