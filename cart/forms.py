from django import forms


class AddToCartProductForm(forms.Form):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 31)]
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput) #widget with this value can dont show this field to user
