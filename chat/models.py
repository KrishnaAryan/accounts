from django.db import models

# Create your models here.
from django.db import models
from accounts.models import *
# Create your models here.
from django.contrib.auth.models import User
from django.db import models
class Message(models.Model):
     sender = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='sender')        
     receiver = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='receiver')        
     message = models.CharField(max_length=1200,null=True,blank=True)
     timestamp = models.DateTimeField(auto_now_add=True)
     document_upload =models.FileField(upload_to='document_upload/',blank=True,null=True)

     is_read = models.BooleanField(default=False)
     def __str__(self):
           return self.message
     class Meta:
           ordering = ('timestamp',)
