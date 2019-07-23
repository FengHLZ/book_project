from django.db import models

# Create your models here.

class BorrowBooks(models.Model):
    b_name = models.CharField(max_length = 30)
    borrowtime = models.DateTimeField(auto_now_add = True)
    stu_id = models.CharField(max_length=10)
    stu_name = models.CharField(max_length=15)
    stu_phone = models.CharField(max_length=11)
    stu_qq = models.CharField(max_length=15)
