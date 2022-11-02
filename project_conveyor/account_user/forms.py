from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator

from project_conveyor.account_user.models import Profile
from django import forms
from django.contrib.auth.models import User

class CreateProfileForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.MAX_LENGTH_FIRST_NAME,
    )
    last_name = forms.CharField(
        max_length=Profile.MAX_LENGTH_LAST_NAME,
    )
    email = forms.EmailField()

    phone_number = forms.IntegerField()

    country = forms.CharField(
        max_length=Profile.MAX_LENGTH_COUNTRY_NAME
    )

    region = forms.ChoiceField(
        choices=Profile.REGION_CHOICE
    )

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            phone_number=self.cleaned_data['phone_number'],
            country=self.cleaned_data['country'],
            region=self.cleaned_data['region'],
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'country', 'region']