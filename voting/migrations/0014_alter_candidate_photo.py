# Generated by Django 5.0.1 on 2024-01-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0013_voter_uvc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='photo',
            field=models.ImageField(blank=True, default='profile1.jpg', null=True, upload_to='candidates'),
        ),
    ]
