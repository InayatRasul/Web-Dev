from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from api.models import Product, Category
# Create your views here.
def show_products(response):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)

def show_product(response, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as dne:
        return JsonResponse({'message': str(dne)}, status=400)
    return JsonResponse(product.to_json())

def show_categories(response):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def show_category(response, id):
    try:
        category = Category.objects.get(id = id)
    except Category.DoesNotExist as dne:
        return JsonResponse({'message': str(dne)}, status = 400)
    return JsonResponse(category.to_json())

def show_category_product(response, id):
    try:
        category_of = Category.objects.get(id = id)
        products = Product.objects.filter(category = category_of.get_name())
        products_json = [product.to_json() for product in products]
    except:
        return JsonResponse({'message': 'There is issue in Category.objects.get or Product.objects.get'})
    return JsonResponse(products_json, safe = False)
