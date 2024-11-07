from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class Address(models.Model):
    objects = models.Manager()
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.house_number}"


class Buyer(models.Model):
    objects = models.Manager()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    special_notes = models.TextField(null=True, blank=True)
    phone_number = models.CharField(
        max_length=12, unique=True,
        validators=[
            RegexValidator(
                regex=r'^\+7\d{10}$',
                message="Введите корректный номер телефона (например, +79991234567)."
            )
        ]
    )
    email = models.EmailField(unique=True)

    addresses = models.ManyToManyField(Address, related_name="buyers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        # Проверка на корректность даты рождения
        if self.date_of_birth and self.date_of_birth > timezone.now().date():
            raise ValidationError("Дата рождения не может быть в будущем.")

    def to_dict(self):
        return {
            "id": self.pk,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "special_notes": self.special_notes,
            "phone_number": self.phone_number,
            "email": self.email,
            "address": [
                {"street": addr.street, "house_number": addr.house_number} for
                addr in self.addresses.all()],
        }
