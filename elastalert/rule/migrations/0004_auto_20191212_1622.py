# Generated by Django 3.0 on 2019-12-12 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule', '0003_auto_20191212_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='runstatus',
            field=models.CharField(default='stopped', max_length=100),
        ),
    ]
