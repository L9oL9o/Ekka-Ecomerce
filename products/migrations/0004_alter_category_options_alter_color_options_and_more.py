# Generated by Django 5.0.1 on 2024-02-15 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_catalog_options_alter_price_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category Model'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name_plural': 'Color Model'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name_plural': 'Currency Model'},
        ),
        migrations.AlterModelOptions(
            name='discount',
            options={'verbose_name_plural': 'Discount Model'},
        ),
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name_plural': 'Price Model'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product Model'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name_plural': 'Product Image Model'},
        ),
    ]