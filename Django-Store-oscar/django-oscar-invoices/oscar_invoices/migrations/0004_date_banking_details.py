# Generated by Django 2.2.13 on 2020-06-05 10:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('oscar_invoices', '0003_auto_20190403_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='legalentity',
            name='bic',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='BIC'),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='iban',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='IBAN'),
        ),
    ]
