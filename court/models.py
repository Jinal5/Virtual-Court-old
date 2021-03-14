from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField

CHOICES = [
    ("Judge", "Judge"),
    ("Lawyer", "Lawyer"),
]

Court_Type=[
    ("SUP","Supreme Court"),
    ("HIG","High Court"),
    ("DST","District Court"),
    ("SES","Session Court"),
]

Case_type=[
    ("CIV","Civil"),
    ("CRI","Criminal"),
]
def user_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'user_{0}/{1}'.format(instance.user.id, filename) 

class UserProfile(models.Model):
    # required by the auth model
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=30, choices=CHOICES)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a matching profile whenever a user object is created."""
    if created:
        profile, new = UserProfile.objects.get_or_create(user=instance)

class Advocate(models.Model):
    license_no = models.CharField(max_length=17, primary_key=True)
    name=models.CharField(max_length=400)
    address=models.CharField(max_length=500)
    court_type=MultiSelectField(choices=Court_Type,max_length=3)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Case(models.Model):
    advocate=models.ForeignKey(Advocate,on_delete=models.CASCADE,related_name="advocate")
    name_of_applicant=models.CharField(max_length=400)
    #phone number
    address=models.CharField(max_length=500)
    case_type=models.CharField(max_length=3,choices=Case_type)
    court_type=models.CharField(choices=Court_Type,max_length=3)
    subject=models.CharField(max_length=500)
    affidavit_fileupload = models.FileField(upload_to = user_directory_path) 


    

# Create your models here.
