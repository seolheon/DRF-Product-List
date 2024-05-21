from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.IntegerField()
    picture = models.ImageField(upload_to='products/', null=True, blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продуткы'
        ordering = ['name']

    def __str__(self):
        return self.name


