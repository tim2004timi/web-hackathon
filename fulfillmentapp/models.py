from django.db import models


class Sellers(models.Model):
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


class Goods(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, default=None)
    owner = models.ForeignKey("Sellers", on_delete=models.CASCADE)

    time_create = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
