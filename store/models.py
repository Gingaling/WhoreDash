from django.db import models

class Category(models.Model):
    name  =  models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
     
    class Meta:
        verbose_name_plural = 'categories'
         
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)
    image = models.ImageField(upload_to='products/images', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    NOTE= models.TextField(blank=True)
    in_stock = models.BooleanField(default=True)
     
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('name',)
        index_together = (('id', 'slug'),)
         
    def __str__(self):
        return self.name
    
     