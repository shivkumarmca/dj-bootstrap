from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'app/home_page.html', {})

def about_view(request):
    return render(request, 'app/about_page.html', {})

def contact_view(request):
    return render(request, 'app/contact_page.html', {})