from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Items(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    barcode = models.IntegerField(db_column='Barcode', blank=True, null=True)  # Field name made lowercase.
    cost = models.IntegerField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    expiration_date = models.DateField(db_column='Expiration_Date', blank=True, null=True)  # Field name made lowercase.
    warehouse = models.ForeignKey('Warehouse', models.DO_NOTHING, db_column='Warehouse_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'items'


class Usergroups(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name
    class Meta:
        #managed = False
        db_table = 'usergroups'


class Users(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='custom_user')

    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100, blank=True, null=True, db_comment='SHA256')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100)  # Field name made lowercase.
    usergroup = models.ForeignKey(Usergroups, models.DO_NOTHING, db_column='Usergroup_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'users'


class Warehouse(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usergroup = models.ForeignKey(Usergroups, models.DO_NOTHING, db_column='Usergroup_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'warehouse'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Usergroup = models.ForeignKey(Usergroups, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    