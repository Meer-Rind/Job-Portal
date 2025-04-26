**Job Portal Website**
A beautifully designed Job Portal web application — helping employers and job seekers connect easily.
Built with Django, TailwindCSS, FontAwesome, and Poppins Google Fonts for a sleek, modern user experience.

**🖌️ Project Overview**
This project serves as a base template (base.html) for a full-fledged Job Portal system.
The frontend is crafted with responsiveness, accessibility, and smooth animations in mind to deliver an excellent user experience for both desktop and mobile users.

**This template provides:**

Responsive Navigation Bar with dynamic user authentication logic

Animated User Notifications (Success, Error, Info)

Dynamic Content Blocks using Django's {% block %} tags

Fully Responsive Mobile Menu with smooth transitions

Custom Tailwind Configuration for colors, fonts, and animations

Reusable Styling Classes for cards, gradients, hover effects, and shadows

Sticky Navigation Bar for better UX

Structured Footer to be extended as per project needs

**📋 Features Explained**

**Feature	Details**
TailwindCSS Integration	Tailwind is included via CDN, with extended custom theme settings.
Custom Font	The elegant Poppins font is used for modern typography.
FontAwesome Icons	FontAwesome 6 icons are used across navigation and alerts.
Dynamic Navigation	Navigation changes based on user roles: Employer, Jobseeker, or Guest.
Flash Messages	Smoothly animated success, error, and info messages for user feedback.
Mobile First Design	Fully responsive with a separate mobile menu and animated transitions.
Custom Animations	Fade-In and Slide-Up animations for better interactivity and UX.
Color Theme	Custom blue-primary gradient based theme for brand consistency.
📂 Technologies Used
#Backend: Django (Python)

**Frontend: HTML5, TailwindCSS (with custom config), FontAwesome**

**Fonts:** Google Fonts (Poppins)

Template Engine: Django Template Language ({% block %}, {% url %}, {% if %})

🚀 How to Use This Template
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/your-username/job-portal.git
cd job-portal
Set up Django Project:

Install Django

Set up the project with basic apps like accounts, jobs

Connect base.html as your main base layout.

Static Files Setup:

Make sure Django is properly serving static files during development.

Use {% load static %} tag at the top as shown.

Extend Base Template:

Create your own pages and extend from base.html:

django
Copy
Edit
{% extends "base.html" %}
{% block title %}Page Title{% endblock %}
{% block content %}
   <!-- Your Page Specific Content -->
{% endblock %}
Add Dynamic URLS:

URLs like {% url 'home' %} will resolve based on your Django URL patterns.

Make sure you have named your URLs correctly in urls.py.

User Authentication System:

The template detects:

If the user is authenticated

Whether they are an employer or jobseeker

Adjust your user model to have flags like is_employer and is_jobseeker.

Responsive Navigation:

The desktop and mobile navigation menus work independently.

Use Tailwind’s hidden md:flex classes to manage visibility across devices.

Flash Messages System:

Django's messages framework is used to display alerts dynamically.

Styles and icons change based on message type (success, error, info).

**📜 Folder Structure Suggestion**
plaintext
Copy
Edit
templates/
 └── base.html
 └── home.html
 └── jobs/
      └── job_list.html
      └── job_detail.html
 └── accounts/
      └── login.html
      └── register.html
static/
 └── css/
 └── js/
 └── images/

 <img width="956" alt="1" src="https://github.com/user-attachments/assets/c428c6fd-6a66-4c80-b121-9e701570de9d" />
<img width="947" alt="2" src="https://github.com/user-attachments/assets/f1b67ae7-93dc-48ab-991e-1b65e2cd329c" />
<img width="957" alt="3" src="https://github.com/user-attachments/assets/8a449b9c-9b2d-463b-97d8-a1478cce203d" />
<img width="887" alt="4" src="https://github.com/user-attachments/assets/9f9d92da-0d1e-4a3c-a4f1-510ce24d5506" />
<img width="883" alt="5" src="https://github.com/user-attachments/assets/7b67b43b-497f-4e72-8215-6632b81f0a75" />

📢 Important Highlights
Gradient Background: linear-gradient for branding colors.

Hover Effects: Buttons and cards gently scale and highlight.

Shadow System: Subtle shadows enhance depth perception on hover.

Sticky Navbar: Navigation remains accessible even while scrolling.

Animation System: Custom fade-in and slide-up keyframes are defined in Tailwind.

**✨ Credits**
Made with ❤️ by Shahmeer Abbas Khan (meer-rind)

**📧 Contact**
If you like this project or want to collaborate, feel free to connect:

**GitHub: meer-rind**

Email: meerdezh@gmail.com

Thank You for Visiting! 🚀
