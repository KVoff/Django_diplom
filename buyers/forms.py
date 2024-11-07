from datetime import date

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Buyer, Address


class BuyerForm(forms.ModelForm):
    addresses = forms.ModelMultipleChoiceField(
        queryset=Address.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Buyer
        fields = ['first_name', 'last_name', 'date_of_birth', 'special_notes',
                  'phone_number', 'email', 'addresses']
        widgets = {
            'date_of_birth': forms.TextInput(attrs={
                'placeholder': 'ГГГГ-ММ-ДД',
            }),
            'special_notes': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
            'phone_number': forms.TextInput(attrs={
                'placeholder': '+79991234567'
            }),
        }
        error_messages = {
            'date_of_birth': {
                'invalid': 'Введите дату в формате ГГГГ-ММ-ДД.'
            },
            'phone_number': {
                'invalid': 'Введите корректный номер телефона (например, +79991234567).'
            }
        }

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        today = timezone.now().date()
        max_age_date = date(today.year - 120, today.month, today.day)

        if date_of_birth:
            if date_of_birth > today:
                raise ValidationError("Дата рождения не может быть в будущем.")
            if date_of_birth < max_age_date:
                raise ValidationError(
                    "Дата рождения не может быть ранее 120 лет назад.")

        return date_of_birth
