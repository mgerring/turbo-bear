from django.db import models

class Signature(models.Model):
	name 		= models.CharField(max_length=256)
	email 		= models.EmailField(max_length=254 ) #why 254 --> https://docs.djangoproject.com/en/dev/ref/models/fields/#emailfield
	subscribe 	= models.BooleanField()
	zipcode		= models.CharField(max_length=10)