from django.db import models


class Headline(models.Model):

    title = models.CharField(max_length=200)
