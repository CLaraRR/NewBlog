from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact


# Create your views here.
def contact_post(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        Contact.objects.create(name = name, email = email, text = text)

    return redirect('blog:contact')







