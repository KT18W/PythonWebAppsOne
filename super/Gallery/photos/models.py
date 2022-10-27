from django.db import models
from django.urls import reverse_lazy

class Hero(models.Model):
    name = models.CharField(max_length=200, default='strengths')
    strengths = models.TextField(max_length=500, default='strengths')
    weaknesses = models.TextField(max_length=500, default='weaknesses')
    identity = models.TextField(max_length=200, default='identity')
    description = models.TextField(max_length=2000, default='description')
    photo = models.CharField(max_length=200, default='/static/images/bad.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('hero_list')