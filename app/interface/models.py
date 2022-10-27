from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Door(models.Model):
    name = models.CharField('Login', max_length=50)
    contact = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="doors")

    def __str__(self):
        return self.name


class History(models.Model):
    time_opening = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user")

    def __str__(self):
        return self.user_name
