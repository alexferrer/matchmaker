# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from .models import Trade

# Register your models here.


class TradeAdmin(admin.ModelAdmin):
    search_fields = ('user',)
    readonly_fields = ('created_at',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == 'user':
                kwargs['queryset'] = User.objects.filter(pk=request.user.id)
                kwargs['initial'] = request.user.id
                kwargs['disabled'] = True

                return db_field.formfield(**kwargs)

        return super(TradeAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        obj = Trade()
        obj.qty = 100
        form = super(TradeAdmin, self).get_form(request, obj, **kwargs)

        if request.user.is_superuser:
            self.fields = ('user', 'qty', 'price', 'status', 'type_of')
        else:
            self.fields = ('user', 'qty', 'price', 'type_of')

        return form


admin.site.register(Trade, TradeAdmin)
