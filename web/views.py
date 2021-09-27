from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *


def home(request):
    service = Service.objects.all()
    home = Home.objects.all()
    service_about = Service_about.objects.all()
    service_model = Service_modal.objects.all()
    service_about2 = Service_about2.objects.all()
    projects = Projects.objects.all()
    testimonials = Testimonials.objects.all()
    pricing = Pricing.objects.all()
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('home')

    context = {
        'service': service,
        'home': home,
        'service_about': service_about,
        'service_model': service_model,
        'service_about2': service_about2,
        'projects': projects,
        'testimonials': testimonials,
        'pricing': pricing,
        'form': form,
    }

    return render(request, 'web/home.html', context)


def article(request):
    return render(request, 'web/article.html')


def terms(request):
    return render(request, 'web/terms.html')


def privacy(request):
    return render(request, 'web/privacy.html')
