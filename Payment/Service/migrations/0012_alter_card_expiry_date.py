# Generated by Django 4.2 on 2023-05-05 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0011_alter_testuser_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='expiry_date',
            field=models.CharField(max_length=16),
        ),
    ]