from email.policy import default
from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    password = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/")
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    door = models.ForeignKey('Door', on_delete=models.PROTECT, verbose_name="What door has access to")

    class Meta:
        ordering = ('id', 'name')
        verbose_name = "Registered user"
        verbose_name_plural = "Registered users"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('info', kwargs={"info_slug": self.slug})


class Door(models.Model):
    name = models.CharField(max_length=50, verbose_name="Company name")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    url = models.URLField(max_length=200, null=True, verbose_name="Link")

    class Meta:
        verbose_name = "Registered door"
        verbose_name_plural = "Registered doors"
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('door', kwargs={"door_slug": self.slug})


class History(models.Model):
    time_opening = models.DateTimeField(auto_now_add=True, db_index=True)

    door = models.ForeignKey('Door', on_delete=models.PROTECT)
    user = models.ForeignKey('User', on_delete=models.PROTECT)

    class Meta:
        ordering = ('-time_opening',)

    def __str__(self):
        return f"{self.user}"

class ErrorLog(models.Model):
    error_name = models.CharField(max_length=1000)
    time_error = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.time_error


class Image(models.Model):
    image = models.ImageField()

    def __str__(self):
        return str(self.image)