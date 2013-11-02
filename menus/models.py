from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=64, unique=True)
    number = models.CharField(max_length=16, unique=True)
    lag = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name

class Option(models.Model):
    menu = models.ForeignKey(Menu)
    level = models.IntegerField()
    tag = models.CharField(max_length=1)
    lag = models.IntegerField(default=0)
    name = models.CharField(max_length=32)
    one = models.IntegerField(default=0)
    one_name = models.CharField(max_length=32)
    two = models.IntegerField(default=0)
    two_name = models.CharField(max_length=32)
    three = models.IntegerField(default=0)
    three_name = models.CharField(max_length=32)
    four = models.IntegerField(default=0)
    four_name = models.CharField(max_length=32)
    five = models.IntegerField(default=0)
    five_name = models.CharField(max_length=32)
    six = models.IntegerField(default=0)
    six_name = models.CharField(max_length=32)
    seven = models.IntegerField(default=0)
    seven_name = models.CharField(max_length=32)
    eight = models.IntegerField(default=0)
    eight_name = models.CharField(max_length=32)
    nine = models.IntegerField(default=0)
    nine_name = models.CharField(max_length=32)
    star = models.IntegerField(default=0)
    star_name = models.CharField(max_length=32)
    zero = models.IntegerField(default=0)
    zero_name = models.CharField(max_length=32)
    hash = models.IntegerField(default=0)
    hash_name = models.CharField(max_length=32)
    def __unicode__(self):
        return self.menu.name+', L='+str(self.level)+self.tag+', '+self.name
    
class User(models.Model):
    number = models.CharField(max_length=16, unique=True)
    def get_number(self):
        return self.number
    def __unicode__(self):
        return self.number
