from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'order_notes']
        widgets = {
            'address': forms.TextInput(attrs={'rows': 3}),
            'order_notes': forms.Textarea(attrs={'rows': 5,
                                                 'placeholder': 'Please write youre note for this order'
                                                 }),
        }