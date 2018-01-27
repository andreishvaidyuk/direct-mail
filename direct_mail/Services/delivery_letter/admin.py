from django.contrib import admin

from .models import DeliveryType, Letter


@admin.register(DeliveryType)
class DeliveryTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ['customer']
    list_filter = ['customer', 'total_price']

    def get_queryset(self, request):
        if not request.user.is_superuser:
            return Letter.objects.filter(customer=request.user)
        return super().get_queryset(request)
