from django.db import models
import datetime
import os
# Create your models here.
def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime('%Y%m%d%h:%M:%S')
    new_filename="%s%s"%(now_time,)
    return os.path.join('uploads/',new_filename)




class Catagory(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)

    quantity = models.IntegerField(null=False,blank=False)
    image = models.CharField(max_length=2083)

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class product(models.Model):
    Category=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=False,blank=False)
    price = models.FloatField()
    quantity = models.IntegerField(null=False,blank=False)
    image = models.CharField(max_length=2083)

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

