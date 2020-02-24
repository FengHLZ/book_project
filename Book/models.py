from django.db import models

# Create your models here.

class BorrowBooks(models.Model):
    b_name = models.CharField("书名", max_length = 30)
    borrowtime = models.DateTimeField("借阅时间", auto_now_add = True)
    stu_id = models.CharField("校园卡号", max_length=10)
    stu_name = models.CharField("借阅者姓名", max_length=15)
    stu_phone = models.CharField("借阅者手机号码", max_length=11)
    stu_qq = models.CharField("借阅者QQ", max_length=15)

class BookDB(models.Model):
    STATUS = (
        ('未借出', '未借出'),
        ('已借出', '已借出'),
    )
    b_name = models.CharField("书名", max_length=50)
    b_img = models.ImageField("书籍封面", upload_to='bookimg')
    b_status = models.CharField("书籍状态", max_length=20, null=True, choices=STATUS)