# Generated by Django 4.1 on 2024-05-17 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis_site', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='thesis',
            constraint=models.UniqueConstraint(fields=('title', 'supervisor'), name='unique_order'),
        ),
    ]
