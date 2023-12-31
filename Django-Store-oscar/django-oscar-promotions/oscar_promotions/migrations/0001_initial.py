# Generated by Django 2.1.1 on 2018-09-02 20:02

from django.db import migrations, models
import django.db.models.deletion
import oscar.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('catalogue', '0013_auto_20170821_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutomaticProductList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('link_url', oscar.models.fields.ExtendedURLField(blank=True, verbose_name='Link URL')),
                ('link_text', models.CharField(blank=True, max_length=255, verbose_name='Link text')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('method', models.CharField(choices=[('Bestselling', 'Bestselling products'), ('RecentlyAdded', 'Recently added products')], max_length=128, verbose_name='Method')),
                ('num_products', models.PositiveSmallIntegerField(default=4, verbose_name='Number of Products')),
            ],
            options={
                'verbose_name': 'Automatic product list',
                'verbose_name_plural': 'Automatic product lists',
            },
        ),
        migrations.CreateModel(
            name='HandPickedProductList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('link_url', oscar.models.fields.ExtendedURLField(blank=True, verbose_name='Link URL')),
                ('link_text', models.CharField(blank=True, max_length=255, verbose_name='Link text')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Hand Picked Product List',
                'verbose_name_plural': 'Hand Picked Product Lists',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('link_url', oscar.models.fields.ExtendedURLField(blank=True, help_text='This is where this promotion links to', verbose_name='Link URL')),
                ('image', models.ImageField(max_length=255, upload_to='images/promotions/', verbose_name='Image')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Image',
            },
        ),
        migrations.CreateModel(
            name='KeywordPromotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('position', models.CharField(help_text='Position on page', max_length=100, verbose_name='Position')),
                ('display_order', models.PositiveIntegerField(default=0, verbose_name='Display Order')),
                ('clicks', models.PositiveIntegerField(default=0, verbose_name='Clicks')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('keyword', models.CharField(max_length=200, verbose_name='Keyword')),
                ('filter', models.CharField(blank=True, max_length=200, verbose_name='Filter')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Keyword Promotion',
                'verbose_name_plural': 'Keyword Promotions',
                'ordering': ['-clicks'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MultiImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('images', models.ManyToManyField(blank=True, help_text='Choose the Image content blocks that this block will use. (You may need to create some first).', to='oscar_promotions.Image')),
            ],
            options={
                'verbose_name': 'Multi Image',
                'verbose_name_plural': 'Multi Images',
            },
        ),
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.PositiveIntegerField(default=0, verbose_name='Display Order')),
            ],
            options={
                'verbose_name': 'Ordered product',
                'verbose_name_plural': 'Ordered product',
                'ordering': ('display_order',),
            },
        ),
        migrations.CreateModel(
            name='PagePromotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('position', models.CharField(help_text='Position on page', max_length=100, verbose_name='Position')),
                ('display_order', models.PositiveIntegerField(default=0, verbose_name='Display Order')),
                ('clicks', models.PositiveIntegerField(default=0, verbose_name='Clicks')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('page_url', oscar.models.fields.ExtendedURLField(db_index=True, max_length=128, verbose_name='Page URL')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Page Promotion',
                'verbose_name_plural': 'Page Promotions',
                'ordering': ['-clicks'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RawHTML',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('display_type', models.CharField(blank=True, help_text='This can be used to have different types of HTML blocks (eg different widths)', max_length=128, verbose_name='Display type')),
                ('body', models.TextField(verbose_name='HTML')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Raw HTML',
                'verbose_name_plural': 'Raw HTML',
            },
        ),
        migrations.CreateModel(
            name='SingleProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Product')),
            ],
            options={
                'verbose_name': 'Single product',
                'verbose_name_plural': 'Single product',
            },
        ),
        migrations.CreateModel(
            name='TabbedBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Title')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
            ],
            options={
                'verbose_name': 'Tabbed Block',
                'verbose_name_plural': 'Tabbed Blocks',
            },
        ),
        migrations.CreateModel(
            name='OrderedProductList',
            fields=[
                ('handpickedproductlist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='oscar_promotions.HandPickedProductList')),
                ('display_order', models.PositiveIntegerField(default=0, verbose_name='Display Order')),
                ('tabbed_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tabs', to='oscar_promotions.TabbedBlock', verbose_name='Tabbed Block')),
            ],
            options={
                'verbose_name': 'Ordered Product List',
                'verbose_name_plural': 'Ordered Product Lists',
                'ordering': ('display_order',),
            },
            bases=('oscar_promotions.handpickedproductlist',),
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oscar_promotions.HandPickedProductList', verbose_name='List'),
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='handpickedproductlist',
            name='products',
            field=models.ManyToManyField(blank=True, through='oscar_promotions.OrderedProduct', to='catalogue.Product', verbose_name='Products'),
        ),
        migrations.AlterUniqueTogether(
            name='orderedproduct',
            unique_together={('list', 'product')},
        ),
    ]
