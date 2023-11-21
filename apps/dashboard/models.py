from django.db import models
from django.utils.text import slugify

# Create your models here

class Category(models.Model):
    title = models.CharField(max_length=100)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Option(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Dataname(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    periode = models.ForeignKey(Option, on_delete=models.CASCADE, null=True)
    source = models.URLField(blank=True)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Dataname, self).save(*args, **kwargs)

class DataValue(models.Model):
    title = models.ForeignKey(Dataname, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    value = models.FloatField(null=True)

    def __str__(self):
        return str(self.title)


