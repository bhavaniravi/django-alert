from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save,pre_delete
from django.dispatch import receiver
from django.apps import apps
from django.contrib import contenttypes
from operator import le,ge,lt,gt,eq
from django.conf import settings

# Create your models here.
class Alert(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300,blank=True,null=True)
    model = models.ForeignKey(contenttypes.models.ContentType)
    field = models.CharField(max_length=100, choices=())
    operation = models.CharField(max_length=10)
    value = models.TextField()
    notification_count = models.PositiveIntegerField()

def parseOp(op):
   op_dict = {">":gt,"<":lt,">=":ge,"<=":le,"=":eq}
   return op_dict[op]

def checkfield(model,field):
   field = model._meta.get_field(field)
   print (field)
   return field

def alert_condition_exist(alerts,sender,instance):
    for alert in alerts:
        op = alert.operation
        #if checkfield(sender,alert.field):
        attr = getattr(instance,alert.field)
        op = parseOp(op)
        print (op)
        if op(attr,alert.value):
            notify.send(alert.owner, alert.owner,"alert triggered ") 
            alert.notification_count += 1
            if not alert == instance:
                alert.save()



@receiver(pre_save,sender=settings.MODELS_TO_CREATE_ALERT)
def common_model_save(sender, instance,**kwargs):
    try:
        ct = contenttypes.models.ContentType.objects.get_for_model(sender)
        alerts = Alert.objects.filter(model=ct)
        print (alerts)
        alert_condition_exist(alerts,sender,instance)
    except ValueError as e:
        print (e)
