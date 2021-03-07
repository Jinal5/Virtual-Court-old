from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

CHOICES = [
    ("Judge", "Judge"),
    ("Lawyer", "Lawyer"),
]


class UserProfile(models.Model):
    # required by the auth model
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=30, choices=CHOICES)
    court = models.CharField(max_length=100, blank=False)
    district = models.CharField(max_length=100, blank=False)
    license_no = models.CharField(max_length=17, null=False)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a matching profile whenever a user object is created."""
    if created:
        profile, new = UserProfile.objects.get_or_create(user=instance)


# Create your models here.
