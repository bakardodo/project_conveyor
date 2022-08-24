from django import forms

from project_conveyor.conveyor_app.models import AskModel, UCFnumber, UCFLbodies, UserPurchases


class CreateAskForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args,**kwargs)
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

class CreateUCFaskform(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        ask_form = super().save(commit=False)

        ask_form.user = self.user
        if commit:
            ask_form.save()
        return ask_form

    class Meta:
        model = UCFnumber
        fields = {'ucf_number'}

# class CreateUCFLForm(forms.ModelForm):
#     def __init__(self, user, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.user = user
#
#     def save(self, commit=True):
#         ucfl_form = super().save(commit=False)
#
#         ucfl_form.user = self.user
#         if commit:
#             ucfl_form.save()
#         return ucfl_form
#
#     class Meta:
#         model = UCFLbodies
#         fields = {'quantity'}

class PurchaseForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        ucfl_form = super().save(commit=False)

        ucfl_form.user = self.user
        if commit:
            ucfl_form.save()
        return ucfl_form

    class Meta:
        model = UserPurchases
        fields = {'quantity'}
