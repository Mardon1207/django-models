from django.views import View
from django.http import HttpRequest, JsonResponse,HttpResponse
from api.models import Product
from django.db.models import Q
from django.forms import model_to_dict
from django.shortcuts import render
import json



class ProductView(View):
    def get(self, request: HttpRequest, pk=None) -> JsonResponse:
        if pk is None:

            query_params = request.GET

            mx = query_params.get('max')
            mn = query_params.get('min')

            if mx is not None and mn is not None:
                products = Product.objects.filter(Q(price__lt=mx) & Q(price__gte=mn)).order_by("price")
            else:
                products = Product.objects.all().order_by("price")

            results = []
            for product in products:
                results.append(model_to_dict(product))

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
        """_summary_

        Args:
            request (HttpRequest): _description_

        Returns:
            JsonResponse: _description_
        """        
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
    
class HomeView(View):
    def get(self,requets)->HttpResponse:
        context={
            'products':Product.objects.all()
        }
        return render(requets,'index.html',context=context)
        