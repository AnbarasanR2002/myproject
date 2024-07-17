# Generated by Django 5.0.6 on 2024-05-27 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestatedetails', '0008_alter_realestate_contact_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=20)),
                ('age', models.IntegerField(max_length=10)),
                ('gender', models.CharField(max_length=20)),
                ('address', models.CharField(default=0, max_length=200)),
                ('qualification', models.CharField(max_length=20)),
                ('occupation', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('account_no', models.PositiveBigIntegerField(default=0)),
                ('ifsc_code', models.CharField(max_length=11)),
                ('bank_name', models.CharField(max_length=20)),
                ('branch_name', models.CharField(max_length=20)),
                ('plots_purchased', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='clientregistration',
        ),
        migrations.AlterField(
            model_name='realestate',
            name='contact_no',
            field=models.PositiveBigIntegerField(),
        ),
    ]
