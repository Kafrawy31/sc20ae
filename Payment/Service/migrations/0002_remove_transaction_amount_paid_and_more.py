# Generated by Django 4.2 on 2023-05-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='amount_paid',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='last_4_digits',
        ),
        migrations.AddField(
            model_name='transaction',
            name='delivery_email',
            field=models.EmailField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='delivery_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='merchant_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]