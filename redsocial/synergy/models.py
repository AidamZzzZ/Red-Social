from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name="following", symmetrical=False, blank=True)
    avatar = models.ImageField(upload_to="users/", default="users/default-profile.jpg", null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
    def follows_count(self):
        user_following = Profile.objects.filter(follows=self)
        return user_following.count()

class Post(models.Model):
    user = models.ForeignKey()
    title = models.CharField(max_length=150)
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)