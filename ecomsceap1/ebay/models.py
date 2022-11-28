from django.db import models

# # Create your models here.
class product_ebay(models.Model):
    id =  models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
