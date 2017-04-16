from django import forms


class ProductAddToCartForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'size': '2',
                                                                'value': '1', 'class': 'input-small',
                                                                'maxlength': '5'}),
                                  error_messages={'invalid': 'Введите правильное количество'}, min_value=1,
                                  label='Количество')
    product_slug = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(ProductAddToCartForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError("Cookies должны быть включены")
        return self.cleaned_data
