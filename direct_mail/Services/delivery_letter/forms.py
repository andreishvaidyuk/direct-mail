from django import forms

from .models import Letter


class BaseLetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        exclude = ('id',)

    def get_total_price(self):
        total_number = 0
        for audience in self.cleaned_data['audience']:
            total_number += audience.number
        return self.instance.delivery_type.price * total_number

    def save(self, commit=True):
        self.instance.total_price = self.get_total_price()
        return super().save(commit=True)


class LetterForm(BaseLetterForm):
    class Meta(BaseLetterForm.Meta):
        exclude = ['total_price']


class LetterOnlyDeliveryForm(BaseLetterForm):
    class Meta(BaseLetterForm.Meta):
        fields = ['audience', 'customer', 'delivery_type']
