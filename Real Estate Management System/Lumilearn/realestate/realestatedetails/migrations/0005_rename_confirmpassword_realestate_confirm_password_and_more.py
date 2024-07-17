# Generated by Django 5.0.6 on 2024-05-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestatedetails', '0004_remove_realestate_contactno_realestate_contactno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realestate',
            old_name='confirmpassword',
            new_name='confirm_password',
        ),
        migrations.RenameField(
            model_name='realestate',
            old_name='contactNo',
            new_name='contact_no',
        ),
        migrations.AddField(
            model_name='realestate',
            name='role',
            field=models.CharField(default='10', max_length=20),
        ),
        migrations.AlterModelTable(
            name='realestate',
            table='REGISTRATION',
        ),
    ]
