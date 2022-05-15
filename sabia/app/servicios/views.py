from django.shortcuts import render
from .models import Product,Category

from django.shortcuts import render, get_object_or_404

from app.cart.forms import CartAddProductForm

from django.contrib.auth.decorators import login_required
# Create your views here.

def esterilizacion(request):

        return render(request, 'servicios/esterilizacion.html')


def pagina_productos(request):

        product = Product.objects.filter(available=True)

        return render(request,"servicios/productos.html",{
                "product": product
        })




def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'servicios/listado_productos.html',
                  {'category': category, 'categories': categories,
                   'products': products})



#def product_detail(request, id, slug):
  #  product = get_object_or_404(Product, id=id, slug=slug, available=True)
   # return render(request, 'servicios/detalle_productos.html', {'product': product})



def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'servicios/detalle_productos.html',
                  {'product': product, 'cart_product_form': cart_product_form})


