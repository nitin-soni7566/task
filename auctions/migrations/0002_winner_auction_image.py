# Generated by Django 4.1.3 on 2023-01-15 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='winner',
            name='auction_image',
            field=models.ImageField(blank=True, max_length=500, upload_to='images'),
        ),
    ]
