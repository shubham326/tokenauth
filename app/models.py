from django.db import models
from django.contrib.auth.models import User


class message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    
    def __str__(self):
        return self.message


#Signals
#token authentication using signal for auto generating token on user regesteration
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils.decorators import method_decorator

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
