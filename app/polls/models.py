from django.db import models


# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)


class Question(models.Model):
    parent_poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.CharField(max_length=128)
    subtext = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_created=True)


class Response(models.Model):
    pass
