from django.shortcuts import render
def index(request):
    return render(request, "index6.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact3.html")

def faq(request):
    return render(request, "faq.html")

def portfolio(request):
    return render(request, "portfolio.html")

def privacypolicy(request):
    return render(request, "privacy_policy.html")

def termscondition(request):
    return render(request, "terms_condition.html")
