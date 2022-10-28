from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name="Employee Name")
    login = models.CharField(max_length=50)
    door = models.ForeignKey('Door', on_delete=models.PROTECT, null=True, verbose_name="What door has access to")

    # event = models.ForeignKey('History', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Door(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="Company name")
    url = models.URLField(max_length=200, null=True, verbose_name="Link")

    def __str__(self):
        return self.name


class History(models.Model):
    time_opening = models.DateTimeField(auto_now_add=True, db_index=True, null=True)

    door = models.ForeignKey('Door', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey('User', on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ('-time_opening',)
    def __str__(self):
        return self.time_opening


class ErrorLog(models.Model):
    error_name = models.CharField(max_length=200)
    time_error = models.DateTimeField(auto_now_add=True, db_index=True)
    door = models.ForeignKey('Door', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey('User', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.time_error
