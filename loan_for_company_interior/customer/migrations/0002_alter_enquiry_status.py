# Generated by Django 4.1.6 on 2023-02-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('Successful', 'Successful'), ('rejected', 'rejected')], default='', max_length=50),
        ),
    ]
