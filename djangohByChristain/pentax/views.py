from django.shortcuts import HttpResponse, render


def hello(request):
    return HttpResponse("<h1>hello world</h1>")


def hello_file(request):
    return render(request, "index.html")


def landing_page(request):
    return render(request, "landingPage.html")


def index(request):
    return render(request, "index.html")
