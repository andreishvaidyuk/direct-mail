from django.db import models

from direct_mail.audience.models import Audience
from direct_mail.users.models import User


class DeliveryType(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Letter(models.Model):
    file = models.FileField(blank=True, null=True)
    delivery_type = models.ForeignKey(DeliveryType,default=1)
    audience = models.ManyToManyField(Audience)
    customer = models.ForeignKey(User, default=1)
    total_price = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.customer.username
