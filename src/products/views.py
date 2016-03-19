from django.shortcuts import render

# Create your views here.

from .models import Product


def details_view(request):
    print request

    product = Product.objects.all().first()
    template = "detail_view.html"
    context = {
        "title": "Detail view",
        "product": product.title
    }
    return render(request, template, context)


def list_view(request):
    print request
    queryset = Product.objects.all()
    template = "list_view.html"
    context = {
        "title": "list view",
        "queryset": queryset
    }
    return render(request, template, context)
