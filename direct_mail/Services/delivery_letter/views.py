from django.views.generic import TemplateView

from .models import DeliveryType

class TypeListView(TemplateView):
    template_name = "delivery_letter/type_list.html"

    def get_context_data(self, **kwargs):
        kwargs['delivery_type_list'] = DeliveryType.objects.all()
        return super().get_context_data(**kwargs)
