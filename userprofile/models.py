from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Profile/', blank=True, null=True)
    cv = models.FileField(upload_to='CV', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.birthdate is None:
            self.birthdate = datetime.today()
        super().save(*args, **kwargs)

    def profile_image(self):
        return (u'<img src="{}" style="width:100px;height:100px;"/>'.format(self.image.url))
    profile_image.short_description = 'Image'
    profile_image.allow_tags = True

# -------------------------------------------------------------------------------------
#  Create User Profile After User Instance is Created
# ------------------------------------------------------------------------------------
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
