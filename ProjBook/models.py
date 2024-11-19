from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço em reais
    pages = models.IntegerField()

    def __str__(self):
        return self.title
