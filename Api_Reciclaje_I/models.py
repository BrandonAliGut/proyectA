from django.db import models
from cloudinary.models import CloudinaryField
import datetime
# Create your models here.


class Category(models.Model):
    name= models.CharField(max_length=50, blank=False)
    img= CloudinaryField("Img_reciclaje_app")
    information  = models.TextField()
    created_at = models.DateField(auto_created=True)
    update_at = models.DateField(default=datetime.datetime.now())