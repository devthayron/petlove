from django.shortcuts import render

def index(request):
    return render(request, 'html/index.html')

def contato(request):
    return render(request, 'html/contato.html')

def product(request):
    return render(request, 'html/product.html')

def servicos(request):
    return render(request, 'html/servicos.html')

def quem_somos(request):
    return render(request, 'html/quem_somos.html')