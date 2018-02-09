from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo (models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    department = models.CharField(max_length=128)

    def __str__(self):
        return self.user.username


class Site(models.Model):
    site_name = models.CharField(max_length=128)
    #client_name = site = models.CharField(max_length=128)
    date_opened = models.CharField(max_length=128)
    crew_list = models.CharField(max_length=128)
    project_manager = models.CharField(max_length=128)
    flowrate = models.CharField(max_length=128)
    current_treatmant= models.CharField(max_length=128)
    #SiteID = site_name

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



class Estimate(models.Model):
    site_name = models.CharField(max_length=128)
    #client_name = site = models.CharField(max_length=128)
    date_opened = models.CharField(max_length=128)
    crew_list = models.CharField(max_length=128)
    project_manager = models.CharField(max_length=128)
    flowrate = models.CharField(max_length=128)
    current_treatmant= models.CharField(max_length=128)
