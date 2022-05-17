from django import forms

from project_conveyor.conveyor_app.models import AskModel


class CreateAskForm(forms.ModelForm):
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