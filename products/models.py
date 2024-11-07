from django.db import models


class Product(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.price}"

    def to_dict(self):
        return {
            "id": self.pk,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "count": self.count,
        }
