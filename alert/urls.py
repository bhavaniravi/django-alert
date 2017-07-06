from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'(?P<model>\w+)/fields?$', views.get_fields, name='fields')
]
