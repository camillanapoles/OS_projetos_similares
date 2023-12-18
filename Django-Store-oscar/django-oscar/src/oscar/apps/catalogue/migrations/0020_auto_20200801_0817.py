# Generated by Django 3.0.8 on 2020-08-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0019_option_required'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ['name'], 'verbose_name': 'Option', 'verbose_name_plural': 'Options'},
        ),
        migrations.AlterField(
            model_name='option',
            name='name',
            field=models.CharField(db_index=True, max_length=128, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='option',
            name='required',
            field=models.BooleanField(default=False, verbose_name='Is this option required?'),
        ),
    ]
