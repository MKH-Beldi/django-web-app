# Generated by Django 4.1 on 2022-08-26 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_rename_band_listings_band'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='like_new',
            field=models.BooleanField(default=False),
        ),
    ]
