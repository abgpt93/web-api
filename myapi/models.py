
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
#from rest_framework.authtoken.models import Token

# Create your models here.
class User(models.Model):
    name = models.CharField(primary_key=True,max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=20)   
    password_confirmation =  models.CharField(max_length=20)

    def _str_(self):
          return self.name

class tweet(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    tweet = models.CharField(max_length=200,null=False,blank=False)
    posted_at = models.DateTimeField(auto_now_add=True, editable=False)


    def _str_(self):
        return self.tweet

'''
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
'''