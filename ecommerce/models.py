from unicodedata import category
from django.db import models

# Create your models here.

class Brand(models.Model):
	brand_name = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.brand_name


class Category(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):

	product_name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	category = models.ManyToManyField(Category)

	def __str__(self):
		return self.product_name




class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	brand = models.ForeignKey(Brand, null=True, on_delete= models.SET_NULL)
	category = models.ForeignKey(Category, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	