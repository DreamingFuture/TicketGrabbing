# Generated by Django 2.2.4 on 2019-08-27 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ticket', '0004_auto_20190814_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='grab',
            name='preach_people',
            field=models.CharField(default='学长学姐', max_length=10, verbose_name='宣讲人'),
        ),
        migrations.AlterField(
            model_name='grab',
            name='times',
            field=models.CharField(max_length=30, verbose_name='宣讲时间'),
        ),
        migrations.AlterField(
            model_name='visitticket',
            name='ticket_id',
            field=models.CharField(default=None, max_length=15, null=True, verbose_name='票号'),
        ),
    ]
