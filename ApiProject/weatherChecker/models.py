from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    title= models.CharField(max_length=50)
    email= models.EmailField(max_length=254)

    # def __str__(self):
    #     return self.name

