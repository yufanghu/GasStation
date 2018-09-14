from django.db import models

# Create your models here.

class auth(models.Model):
    pass
    # user = models.CharField(max_length=30)
    # fromsite = models.CharField(max_length=50)
    # bookname = models.CharField(max_length=50)
    #updatetime = models.DateTimeField()
    #lastchapter = models.CharField(max_length=100)

class site_info(models.Model):
    pass
    # sitename = models.CharField(max_length=50)
    # bookname = models.CharField(max_length=50)
    # url = models.CharField(max_length=200)
    # updatetime = models.DateTimeField()
    # lastchapter = models.CharField(max_length=100)

#告警数据
class tbl_warning(models.Model):
    deviceid=models.IntegerField(default=0)
    createtime=models.DateTimeField()
    warningDetail=models.CharField(max_length = 1024)

#设备
class tbl_device(models.Model):
    deviceid=models.IntegerField(primary_key=True)
    devicename=models.CharField(max_length = 256)
