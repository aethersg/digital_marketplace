from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Product


def details_view(request, object_id):
    if request.user.is_authenticated():
        if object_id is not None:
            try:
                product = get_object_or_404(Product, id=object_id)
            except ValueError:
                raise Http404
            template = "detail_view.html"
            context = {
                "title": "Detail view",
                "product": product.title
            }
            return render(request, template, context)
        else:
            raise Http404
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
