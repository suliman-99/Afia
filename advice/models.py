from django.db import models


class Advice(models.Model):
    content = models.TextField()
    
