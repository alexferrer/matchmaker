# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Trade(models.Model):
    BUY = 1
    SELL = 2

    TYPES = (
        (BUY, 'BUY'),
        (SELL, 'SELL')
    )

    CLOSE = 0
    OPEN = 1
    PENDING = 2

    STATUSES = (
        (CLOSE, 'CLOSE'),
        (OPEN, 'OPEN')
    )

    user = models.ForeignKey(User, blank=False, null=False)
    qty = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(
        max_digits=11, decimal_places=2, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUSES, default=OPEN)
    type_of = models.IntegerField(choices=TYPES, default=BUY)

    class Meta:
        pass

    def __unicode__(self):
        return "{action}: {user} - {qty} to {price} (unit price)".format(
            action=self.TYPES[self.type_of - 1][1],
            user=self.user,
            qty=self.qty,
            price=self.price)
