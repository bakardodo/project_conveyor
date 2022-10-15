from django import forms
from django.forms import HiddenInput

from project_conveyor.conveyor_app.models import AskModel, ShippingAdress


class CreateAskForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        ask_form = super().save(commit=False)

        ask_form.user = self.user
        if commit:
            ask_form.save()
        return ask_form

    type_of_tape = forms.ChoiceField(choices=AskModel.TYPE_TEXTILE, label='Вид лента')
    connection_method = forms.ChoiceField(choices=AskModel.TYPE_CONNECTION, label='Начин на свързване')
    class Meta:
        model = AskModel
        fields = ('name', 'telephone', 'type_of_tape', 'connection_method', 'width', 'length', 'blade_height', 'blade_length', 'step_between_blades', 'height_of_side_stops', 'description')
        widgets = {
            'width' : forms.TextInput(
                attrs={
                    'placeholder': 'см',
                }
            ),
            'length': forms.TextInput(
                attrs={
                    'placeholder': 'см',
                }
            ),
            'blade_height': forms.TextInput(
                attrs={
                    'placeholder': 'см',
                }
            ),
            'blade_length': forms.TextInput(
                attrs={
                    'placeholder': 'см',
                }
            ),
            'step_between_blades': forms.TextInput(
                attrs={
                    'placeholder': 'см',
                }
            ),
            'height_of_side_stops': forms.TextInput(
                attrs={
                    'placeholder': 'см',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Допълнителна информация',
                }
            ),

        }

class ShippingAddressForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        shipping_address = super().save(commit=False)

        shipping_address.user = self.user
        if commit:
            shipping_address.save()
        return shipping_address

    class Meta:
        model = ShippingAdress
        fields = ('email', 'address', 'city', 'state', 'zipcode')
        # widgets = {
        #     'email': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Въведете вашият имейл',
        #         }
        #     ),
        #     'address': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Адрес за доставка',
        #         }
        #     ),
        #     'city': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Въведете вашият град',
        #         }
        #     ),
        #     'state': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Въведете вашият имейл',
        #         }
        #     ),
        #     'zipcode': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Въведете вашият имейл',
        #         }
        #     ),