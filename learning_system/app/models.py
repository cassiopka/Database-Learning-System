from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'

class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=255)
    video_link = models.URLField()

    def __str__(self):
        return self.name

class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, through=ProductAccess, related_name='my_groups')

    def __str__(self):
        return self.name