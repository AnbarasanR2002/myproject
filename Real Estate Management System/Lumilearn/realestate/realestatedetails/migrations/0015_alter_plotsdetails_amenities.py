# Generated by Django 5.0.6 on 2024-06-05 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestatedetails', '0014_alter_plotinfo_amenities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plotsdetails',
            name='amenities',
            field=models.CharField(max_length=200),
        ),
    ]
