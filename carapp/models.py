from django.db import models

class carlist(models.Model):
	BrandName = models.CharField(max_length=100)
	ModelName = models.CharField(primary_key=True,max_length=100)
	Fuels = models.CharField(max_length=100)
	Price = models.IntegerField()  

	
# Create your models here.
