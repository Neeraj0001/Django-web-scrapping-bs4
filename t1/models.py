from django.db import models

# Create your models here.
class Scrapping(models.Model):
    ID = models.AutoField
    Site_URL = models.CharField(max_length=500)
    Top_word = models.CharField(max_length=500)
    def __str__(self):
    	return self.Site_URL

