from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Seller(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    login = models.CharField(max_length=20, primary_key=True, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(blank=True, default=None)
    telegram = models.CharField(max_length=30, blank=True, default=None)
    time_signup = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.login


class Operator(models.Model):
    login = models.CharField(max_length=20, primary_key=True, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.login


class Product(models.Model):
    article = models.IntegerField(validators=[MinValueValidator(10000)], default=10001, primary_key=True, unique=True)
    name = models.CharField(default=None, max_length=30)
    size = models.CharField(default=None, max_length=30)
    color = models.CharField(default=None, max_length=30)
    numbers = models.IntegerField(default=1, validators=[MaxValueValidator(100)])
    seller = models.ForeignKey("Seller", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default=None, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Delivery(models.Model):
    product = models.OneToOneField("Product", on_delete=models.CASCADE, primary_key=True)
    address = models.TextField()
    driver_fio = models.CharField(max_length=50)
    car_number = models.CharField(max_length=20)
    date = models.DateField()
    qr = models.ImageField()

    objects = models.Manager()

    def __str__(self):
        return f"{self.product.name} отгрузка"
