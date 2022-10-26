from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)





class User(models.Model):
    name = models.CharField('Name', max_length=50)
    login = models.CharField('', max_length=50)

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
