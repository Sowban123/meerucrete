from django.shortcuts import render, get_object_or_404
from .models import Slide, Contact, Project
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# ---------------- Home Page ----------------
def index(request):
    slides = Slide.objects.all()
    projects = Project.objects.all()[:2]  # Show first 4 projects on homepage
    return render(request, 'index.html', {'slides': slides, 'projects': projects})

# ---------------- Contact Page ----------------
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        # Save to database
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()

        # Send email notification
        subject = "New Contact Form Submission"
        body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message:
        {message}
        """
        send_mail(subject, body, settings.EMAIL_HOST_USER, ['mohammedsowban008@gmail.com'], fail_silently=False)

        messages.success(request, "Thank you for contacting us!")

    return render(request, 'contactus.html')

# ---------------- About Page ----------------
def about_view(request):
    return render(request, 'about.html')

# ---------------- Product Page ----------------
def product_view(request):
    return render(request, 'product.html')

from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    features_list = project.features.split(',') if project.features else []

    return render(request, 'project_detail.html', {
        'project': project,
        'features_list': features_list
    })

# views.py
from django.shortcuts import render
from .models import ProductCollection, ProductCatalogue

# Collection page
def product_section(request):
    series = ProductCollection.objects.prefetch_related('cards').all()
    return render(request, 'product.html', {'series': series})

# Catalogue page
def product_catalogue_view(request):
    series = ProductCatalogue.objects.prefetch_related('cards').all()
    return render(request, 'product2.html', {'series': series})










# shop/views.py
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import ProductEnquiry
from django.conf import settings

def save_enquiry(request):
    if request.method == 'POST':
        product_name = request.POST.get('productName')
        address = request.POST.get('address')
        state = request.POST.get('state')
        mobile = request.POST.get('mobile')
        message_text = request.POST.get('message')

        # Save to database
        ProductEnquiry.objects.create(
            product_name=product_name,
            address=address,
            state=state,
            mobile=mobile,
            message=message_text
        )

        # Send email notification
        subject = f"New Product Enquiry: {product_name}"
        body = f"""
        You have received a new product enquiry.

        Product: {product_name}
        Address: {address}
        State: {state}
        Mobile: {mobile}
        Message: {message_text}
        """
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,  # Your email from settings.py
            ['nnahmed.1982@gmail.com'],  # Replace with the email that should receive notifications
            fail_silently=False,
        )

        messages.success(request, "Your enquiry has been submitted successfully!")
        return redirect('product_section')  # Redirect after submission

    return redirect('product_section')
