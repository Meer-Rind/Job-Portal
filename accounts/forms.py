from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, JobSeeker, Employer

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=17)
    profile_picture = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'profile_picture', 'password1', 'password2']

class JobSeekerSignUpForm(UserRegisterForm):
    resume = forms.FileField(required=False)
    skills = forms.CharField(widget=forms.Textarea, required=False)
    education = forms.CharField(widget=forms.Textarea, required=False)
    experience = forms.CharField(widget=forms.Textarea, required=False)
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_jobseeker = True
        if commit:
            user.save()
            jobseeker = JobSeeker.objects.create(
                user=user,
                skills=self.cleaned_data.get('skills'),
                education=self.cleaned_data.get('education'),
                experience=self.cleaned_data.get('experience')
            )
            if self.cleaned_data.get('resume'):
                user.resume = self.cleaned_data.get('resume')
                user.save()
        return user

class EmployerSignUpForm(UserRegisterForm):
    company_name = forms.CharField(max_length=100)
    company_description = forms.CharField(widget=forms.Textarea, required=False)
    company_website = forms.URLField(required=False)
    company_logo = forms.ImageField(required=False)
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employer = True
        if commit:
            user.save()
            employer = Employer.objects.create(
                user=user,
                company_name=self.cleaned_data.get('company_name'),
                company_description=self.cleaned_data.get('company_description'),
                company_website=self.cleaned_data.get('company_website')
            )
            # Handle the company logo separately
            if 'company_logo' in self.files:
                employer.company_logo = self.files['company_logo']
                employer.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=17)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'profile_picture']

class JobSeekerUpdateForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ['skills', 'education', 'experience']

class EmployerUpdateForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['company_name', 'company_description', 'company_website', 'company_logo']