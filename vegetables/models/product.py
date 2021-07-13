from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category =models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description =models.CharField(max_length=1000,default='')
    description1 =models.CharField(max_length=1000,default='')
    description2 =models.CharField(max_length=1000,default='')
    
    benefits =models.CharField(max_length=1000,default='')
    benefits1 =models.CharField(max_length=1000,default='')
    benefits2 =models.CharField(max_length=1000,default='')
    
    
    image = models.ImageField(upload_to='uploads/products/')
    image1 = models.ImageField(upload_to='uploads/products/',default="")
    image2 = models.ImageField(upload_to='uploads/products/',default="")

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_categories_by_id(category_id):


        if category_id:
            return Product.objects.filter(category= category_id)
        else:
            return Product.get_all_products()


    @staticmethod
    def get_all_products_by_id(id):


        if id:
            return Product.objects.get(id= id)
        else:
            return Product.get_all_products()
   