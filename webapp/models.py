from django.db import models

# Create your models here.

class Product(models.Model):
    name_of_product = models.CharField(max_length=200, null=False, blank=False, verbose_name='Наименование товара')
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False, verbose_name='Стоимость')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.name_of_product
