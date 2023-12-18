# Generated by Django 3.2.8 on 2021-10-27 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0025_attribute_code_uniquetogether_constraint'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ['order', 'name'], 'verbose_name': 'Option', 'verbose_name_plural': 'Options'},
        ),
        migrations.AddField(
            model_name='option',
            name='help_text',
            field=models.CharField(blank=True, help_text='Help text shown to the user on the add to basket form', max_length=255, null=True, verbose_name='Help text'),
        ),
        migrations.AddField(
            model_name='option',
            name='option_group',
            field=models.ForeignKey(blank=True, help_text='Select an option group if using type "Option" or "Multi Option"', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_options', to='catalogue.attributeoptiongroup', verbose_name='Option Group'),
        ),
        migrations.AddField(
            model_name='option',
            name='order',
            field=models.IntegerField(blank=True, db_index=True, help_text='Controls the ordering of product options on product detail pages', null=True, verbose_name='Ordering'),
        ),
        migrations.AlterField(
            model_name='option',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('integer', 'Integer'), ('boolean', 'True / False'), ('float', 'Float'), ('date', 'Date'), ('select', 'Select'), ('radio', 'Radio'), ('multi_select', 'Multi select'), ('checkbox', 'Checkbox')], default='text', max_length=255, verbose_name='Type'),
        ),
    ]
