from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Item(models.Model):
   text = models.TextField(default="")  
   list = models.ForeignKey("List", default=None)

class List(models.Model):
#   id = models.AutoField(primary_key=True) 
   def get_absolute_url(self):
      return reverse("view_list", args=[self.id])
 
