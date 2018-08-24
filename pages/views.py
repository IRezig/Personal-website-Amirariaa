from django.shortcuts import render


def home(request):
    return render(request, "home.html", {})


def about(request):
    return render(request, "about.html", {})


def abayatgallery(request):
    return render(request, "abayatgallery.html", {})


def burkinigallery(request):
    return render(request, "burkinigallery.html", {})


def contactezmoi(request):
    return render(request, "contactezmoi.html", {})


def defiledemode(request):
    return render(request, "defiledemode.html", {})


def summergallery(request):
    return render(request, "summergallery.html", {})


def eidgallery(request):
    return render(request, "eidgallery.html", {})


def scarfgallery(request):
    return render(request, "scarfgallery.html", {})
