from django.views import View
from django.http import HttpRequest, JsonResponse
from api.models import Product
import json



class ProductView(View):
    def get(self, request: HttpRequest, pk=None) -> JsonResponse:
        if pk is None:
            products = Product.objects.all()

            results = []
            for product in products:
                results.append({
                    "id": product.id,
                    "name": product.name,
                    "description": product.description,
                    "price": product.price,
                })

            return JsonResponse(results, safe=False)
        else:
            product = Product.objects.get(id=pk)
            
            results = {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
            }
            return JsonResponse(results)

    def post(self, request: HttpRequest) -> JsonResponse:
        body = request.body.decode()
        data = json.loads(body)

        Product.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price')
        )
        return JsonResponse({'message': 'object created.'}, status=201)

    def put(self, request: HttpRequest,pk=None) -> JsonResponse:
        body = request.body.decode()
        data = json.loads(body)
        product=Product.objects.get(id=pk)
        product.name=data.get('name',product.name)
        product.description=data.get('description',product.description)
        product.price=data.get('price',product.price)
        product.save()
        return JsonResponse({'message':'update'})



    def delete(self, request: HttpRequest, pk=None) -> JsonResponse:
            produkt=Product.objects.get(id=pk)
            produkt.delete()
            return JsonResponse({'message': 'deleted.'}, status=200)
        