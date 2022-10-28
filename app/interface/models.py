from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    door_id = models.ForeignKey('Door', on_delete=models.PROTECT, null=True)
    event = models.ForeignKey('History', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Door(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name


class History(models.Model):
    time_opening = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.time_opening
