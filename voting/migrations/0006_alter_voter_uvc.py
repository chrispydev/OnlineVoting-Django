# Generated by Django 5.0.1 on 2024-01-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_alter_voter_uvc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='uvc',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]