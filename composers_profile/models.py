from django.db import models
from django.contrib.auth.models import User

from oauth2client.django_orm import FlowField
from oauth2client.django_orm import CredentialsField

class ComposersProfile(models.Model):
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length="100")
    last_name = models.CharField(max_length="100")
    gender = models.CharField(max_length="1", choices=gender)
    address = models.CharField(max_length="100")
    latitude = models.FloatField()
    longitude = models.FloatField()
    current_song = models.CharField(max_length="100")
    hit_songs = models.CharField(max_length="100")
    education = models.CharField(max_length="100")
    summary = models.CharField(max_length="100")

    def __unicode__(self):
        return u'%s' % (self.first_name)


class ForgotPasswordUsers(models.Model):
    token = models.CharField(max_length="100")
    flag = models.BooleanField(default = False)
    forgotpassworduser = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' %(self.forgotpassworduser.first_name)


class FlowModel(models.Model):
    id = models.ForeignKey(User, primary_key=True)
    flow = FlowField()


class CredentialsModel(models.Model):
    id = models.ForeignKey(User, primary_key=True)
    credential = CredentialsField()
