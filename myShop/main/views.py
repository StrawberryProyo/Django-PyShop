from django.shortcuts import render

def index(request):
    return render(request, 'pages/home.html')

def products(request):
    return render(request, 'pages/products.html')

def transactions(request):
    return render(request, 'pages/transac.html')

def settings_page(request):
    return render(request, 'pages/settings.html')

def cart(request):
    return render(request, "pages/modals/cart.html")

def wishlist(request):
    return render(request, "pages/modals/wishlist.html")

def checkout(request):
    return render(request, "pages/modals/checkout.html")

def address(request):
    return render(request, "pages/modals/address.html")