# Generated by Django 5.0.6 on 2024-06-04 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestatedetails', '0010_bi_client_req_plotinfo_plotsdetails_sellers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plotinfo',
            name='square_feet',
        ),
    ]
