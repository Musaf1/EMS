from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save # when user created send signal to create provile
from django.dispatch import receiver
# this class for user to update his info 
class Profile(models.Model):
    user = models.OneToOneField(User , null=True , on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 20,null = True )
    profile_image = models.ImageField(upload_to='profiles',default='default.png',blank=True,null=True,help_text='upload image size less than 2.0MB')#work on path username-date/image
    date_created = models.DateTimeField(auto_now_add =True, null = True)
    date_modified = models.DateTimeField(User , auto_now=True)
    # relation ,  managers to employees , use follows to see who is your manager , followed by see who is your employees
    follows = models.ManyToManyField("self", 
                                     related_name="followed_by", # who follow you 
                                     symmetrical=False,
                                     blank=True)
    def __str__(self):
#        return self.user.username
        return self.name # to show name 
    
# when user created send signal to create provile
@receiver(post_save, sender = User)
def create_profile(sender, instance, created,**kwargs):
    if created: 
        user_profile = Profile(user = instance)
        user_profile.save()