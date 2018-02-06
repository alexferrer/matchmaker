# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Trade
from django.views.generic.edit import CreateView


class TradeForm(CreateView):
    model = Trade
    fields = ['type_of', 'qty', 'price']
    success_url = '/trade/create/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TradeForm, self).form_valid(form)
