# Generated by Django 2.1.7 on 2019-12-05 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0004_auto_20191205_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdb',
            name='b_status',
            field=models.CharField(max_length=20, null=True, verbose_name='书籍状态'),
        ),
    ]
