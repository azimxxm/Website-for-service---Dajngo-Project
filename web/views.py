from django.shortcuts import render

def home(request):
    return render(request, 'web/home.html')

def article(request):
    return render(request, 'web/article.html')

def terms(request):
    return render(request, 'web/terms.html')

def privacy(request):
    return render(request, 'web/privacy.html')

