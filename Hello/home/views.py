from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'variable': 'This is sent'
    }
    # Render the index.html template
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is the about page.")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is the services page.")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, mobile=mobile, message=message, date=datetime.today())
        contact.save()
        messages.success(request, "Your Message has been sent")
    return render(request, 'contact.html')
    #return HttpResponse("This is the contact page.")