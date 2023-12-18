# Generated by Django 2.2.4 on 2019-08-16 08:38

from django.db import migrations, models
import oscar.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0016_auto_20190327_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattributevalue',
            name='value_file',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=oscar.utils.models.get_image_upload_path),
        ),
        migrations.AlterField(
            model_name='productattributevalue',
            name='value_image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=oscar.utils.models.get_image_upload_path),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='original',
            field=models.ImageField(max_length=255, upload_to=oscar.utils.models.get_image_upload_path, verbose_name='Original'),
        ),
    ]
