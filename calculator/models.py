from django.db import models
from django.forms import ModelForm, Textarea, forms

# Create your models here.

class Inventory(models.Model):
    inventory_paste = models.CharField(max_length=1024)

