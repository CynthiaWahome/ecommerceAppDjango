from django.shortcuts import get_object_or_404, render
from . models import Customer, Product

# Create your views here.

def home(request):
    return render(request, 'ecommerceApp/home.html')

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
        }
    return render(request,'ecommerceApp/product_list.html',context)

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
            'product': product
            }
    return render(request, 'ecommerceApp/product_details.html', context)

def customer_list(request):
    customers = Customer.objects.all()
    context = {
            'customers': customers
            }
    return render(request, 'ecommerceApp/customer_list.html', context)

def customer_details(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context = {
            'customers' : customer

    }
    return render(request, 'ecommerceApp/customer_details.html', context)


    
# Create your views here.
