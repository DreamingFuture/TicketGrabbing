# Generated by Django 2.2.4 on 2019-08-14 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ticket', '0003_auto_20190810_0953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grab',
            options={'verbose_name': '宣讲会管理', 'verbose_name_plural': '宣讲会管理'},
        ),
        migrations.AlterModelOptions(
            name='visitticket',
            options={'verbose_name': '参观学生管理', 'verbose_name_plural': '参观学生管理'},
        ),
        migrations.AlterField(
            model_name='grab',
            name='ticket_id',
            field=models.CharField(default=None, max_length=15, null=True, verbose_name='票号'),
        ),
    ]
