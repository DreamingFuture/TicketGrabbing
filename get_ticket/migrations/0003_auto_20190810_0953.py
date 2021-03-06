# Generated by Django 2.2.4 on 2019-08-10 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ticket', '0002_auto_20190809_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, verbose_name='姓名')),
                ('stu_id', models.CharField(max_length=10, verbose_name='学号')),
                ('major', models.CharField(max_length=50, verbose_name='专业')),
                ('times', models.CharField(max_length=30, verbose_name='预约时间')),
                ('is_success', models.BooleanField(default=False, verbose_name='是否抢票成功')),
                ('is_checked', models.BooleanField(default=False, verbose_name='是否已检票')),
                ('ticket_id', models.CharField(max_length=15, null=True, verbose_name='票号')),
            ],
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
        migrations.AddField(
            model_name='visitticket',
            name='is_checked',
            field=models.BooleanField(default=False, verbose_name='是否已检票'),
        ),
    ]
