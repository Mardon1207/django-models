from django.views import View
from .models import Person
from django.http import HttpRequest, JsonResponse



class PersonView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        person = Person.objects.last()

        result = {
            'id': person.id,
            'first_name': person.first,
            'last_name': person.last,
        }
        
        return JsonResponse(result)