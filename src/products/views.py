from django.shortcuts import render

# Create your views here.

from .models import Product


def details_view(request):
    if request.user.is_authenticated():
        product = Product.objects.all().first()
        template = "detail_view.html"
        context = {
            "title": "Detail view",
            "product": product.title
        }
    else:
        template = "not_found.html"
        context = {}
    return render(request, template, context)


def list_view(request):
    if request.user.is_authenticated():
        queryset = Product.objects.all()
        template = "list_view.html"
        context = {
            "title": "list view",
            "queryset": queryset
        }
    else:
        template = "not_found.html"
        context = {}
    return render(request, template, context)
