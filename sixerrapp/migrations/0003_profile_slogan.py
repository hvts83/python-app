# Generated by Django 3.0.4 on 2020-03-23 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sixerrapp', '0002_gig'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slogan',
            field=models.CharField(default='My Slogan', max_length=500),
            preserve_default=False,
        ),
    ]
