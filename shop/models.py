from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, null=True)
    image = models.ImageField(upload_to='media/')
    description = models.TextField()

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, null=True)
    image = models.ImageField(upload_to='media/')
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


