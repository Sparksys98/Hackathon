from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
# Create your models here.
class WishModel(models.Model):
    name=models.CharField(max_length=100)
    url=models.URLField(null= True, blank=True)
    img=models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField('date created', default=timezone.now)
    person = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    completed = models.BooleanField(null=False,default=False)
    # unique_id = ListModel()  
class ListModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
