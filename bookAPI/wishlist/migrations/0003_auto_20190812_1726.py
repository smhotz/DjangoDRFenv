# Generated by Django 2.1.11 on 2019-08-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_auto_20190810_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='bid',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
