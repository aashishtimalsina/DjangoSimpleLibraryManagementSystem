from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class bookCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateField()
    cover = models.ImageField(upload_to='covers/')
    categories = models.ManyToManyField(bookCategory)

    def __str__(self):
        return self.title

class bookOrder(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    coupon = models.CharField(max_length=50, blank=True, null=True)
    is_received = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_name
    
