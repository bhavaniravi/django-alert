from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.apps import apps


def get_model(model):
   for m in apps.get_models():
       if m.__name__.lower() == model:
           return m
# Create your views here.
def get_fields(request,model):
    if request.method == "GET":
        model = get_model(model)
        fields = [field.name for field in model._meta.get_fields()]
        return JsonResponse(fields,safe=False)
