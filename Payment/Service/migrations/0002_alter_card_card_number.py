# Generated by Django 4.2 on 2023-04-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(max_length=19, primary_key=True, serialize=False, unique=True),
        ),
    ]