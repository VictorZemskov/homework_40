from django.shortcuts import render
from webapp.models import Product
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.


def index_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)

def products_view(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    elif request.method == 'POST':
        product = Product.objects.create(
            name_of_product=request.POST.get('name_of_product'),
            description=request.POST.get('content'),
            price=request.POST.get('price')
        )
        return HttpResponseRedirect(reverse('product__view', args=[product.pk]))


def product_view(request, product_pk):
    try:
        product = Product.objects.get(pk=product_pk)
    except Product.DoesNotExist:
        raise Http404
    context = {
        'product': product
    }
    return render(request, 'view.html', context)

def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request, 'contacts.html')