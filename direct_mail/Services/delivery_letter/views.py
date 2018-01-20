from django.shortcuts import render

from django.views.generic import TemplateView


class TypeListView(TemplateView):
    template_name = "delivery_letter/type_list.html"
