from distutils.command.upload import upload
from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=100, unique=True)
    description = models.TextField(verbose_name="описание", blank=True)

    def __str__(self):
        return self.name

class ProductManager(models.Manager):
    def active_items(self):
        return Product.objects.filter(is_active=True)


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="имя", max_length=100)
    price = models.DecimalField(
        verbose_name="цена", max_digits=7, decimal_places=2, default=0
    )
    color = models.PositiveBigIntegerField(verbose_name="цвет", default=0x000000)
    description = description = models.TextField(verbose_name="описание", blank=True)
    image = models.ImageField(verbose_name="картинка", blank=True, upload_to="products")
    quantity = models.PositiveBigIntegerField(verbose_name="количество", default=0)
    is_active = models.BigIntegerField(verbose_name="активный", default=True)

    objects = ProductManager()


    def __str__(self):
        return self.name