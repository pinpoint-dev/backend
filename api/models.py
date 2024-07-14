from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# user model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    Name = models.CharField(max_length=50, null=True, blank=True)
    main_device = models.OneToOneField('Device', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=50, null=True, blank=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.CharField(max_length=7)
    location = models.CharField(max_length=50, null=True, blank=True)
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name