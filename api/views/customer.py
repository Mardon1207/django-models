from django.views import View
from django.http import HttpRequest, JsonResponse
from api.models import Customer
import json


class CustomerView(View):
    def get(self, request: HttpRequest, pk=None) -> JsonResponse:
        if pk is None:
            customers = Customer.objects.all()

            query_params=request.GET

            age=query_params.get('age')
            if age is not None:
                customers=Customer.objects.filter(age=age)
            else:
                customers = Customer.objects.all()
            results = []
            for customer in customers:
                results.append({
                    "id": customer.id,
                    "first_name": customer.first_name,
                    "last_name": customer.last_name,
                    "phone_number": customer.phone_number,
                    "email": customer.email,
                    "address": customer.address,
                    "birth_day": customer.birth_day,
                    "joined_date": customer.joined_date,
                    "gender": customer.gender,
                    "age": customer.age,
                    "username": customer.username
                })

            return JsonResponse(results, safe=False)
        else:
            customer = Customer.objects.get(id=pk)
            
            results = {
                "id": customer.id,
                    "first_name": customer.first_name,
                    "last_name": customer.last_name,
                    "phone_number": customer.phone_number,
                    "email": customer.email,
                    "address": customer.address,
                    "birth_day": customer.birth_day,
                    "joined_date": customer.joined_date,
                    "gender": customer.gender,
                    "age": customer.age,
                    "username": customer.username
            }
            return JsonResponse(results)
    def post(self, request: HttpRequest) -> JsonResponse:
        body = request.body.decode()
        data = json.loads(body)

        Customer.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            phone_number=data.get('phone_number'),
            email=data.get('email'),
            address=data.get('address'),
            birth_day=data.get('birth_day'),
            joined_date=data.get('joined_date'),
            gender=data.get('gender'),
            age=data.get('age'),
            username=data.get('username')
        )
        return JsonResponse({'message': 'object created.'}, status=201)
    def put(self, request: HttpRequest,pk=None) -> JsonResponse:
        body = request.body.decode()
        data = json.loads(body)
        customer=Customer.objects.get(id=pk)
        customer.first_name=data.get('first_name',customer.first_name)
        customer.last_name=data.get('last_name',customer.last_name)
        customer.phone_number=data.get('phone_number',customer.phone_number)
        customer.email=data.get('email',customer.email)
        customer.address=data.get('address',customer.address)
        customer.birth_day=data.get('birth_day',customer.birth_day)
        customer.joined_date=data.get('joined_date',customer.joined_date)
        customer.gender=data.get('gender',customer.gender)
        customer.username=data.get('username',customer.username)

        customer.save()
        return JsonResponse({'message':'update'})
    def delete(self, request: HttpRequest, pk=None) -> JsonResponse:
            produkt=Customer.objects.get(id=pk)
            produkt.delete()
            return JsonResponse({'message': 'deleted.'}, status=200)