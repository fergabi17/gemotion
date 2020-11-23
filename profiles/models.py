from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    """
    A user profile module 
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    donated = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_or_update_user(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users just save the profile
    instance.userprofile.save()
    
    