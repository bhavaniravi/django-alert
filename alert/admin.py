from django.contrib import admin
from .models import *
# Register your models here.
from django import forms
from django.conf import settings

# class AlertForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(AlertForm, self).__init__(*args, **kwargs)
#         self.fields['field'] = forms.ChoiceField(
#             choices=[]
#         )
#         self.fields['model'].queryset = self.fields['model'].queryset.filter(model__in=settings.MODELS_TO_CREATE_ALERT)
#     class Media:
#         js = ["//ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js",
#               '/static/custom.js']
#     class Meta:
#         model = Alert
#         fields = '__all__'

# class AlertAdmin(admin.ModelAdmin):
#     form = AlertForm

admin.site.register(Alert)
