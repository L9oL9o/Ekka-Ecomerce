# Generated by Django 5.0.1 on 2024-02-11 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='count',
            field=models.PositiveIntegerField(default=10, verbose_name='Count'),
        ),
        migrations.AddField(
            model_name='discount',
            name='slug',
            field=models.SlugField(default=1, max_length=255, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discount',
            name='text',
            field=models.TextField(default=1, max_length=255, verbose_name='Text'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=255, verbose_name=' Name'),
        ),
        migrations.AlterField(
            model_name='color',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='name',
            field=models.CharField(max_length=255, verbose_name=' Name'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='percentage',
            field=models.PositiveIntegerField(default=0, verbose_name='Percentage'),
        ),
        migrations.AlterField(
            model_name='price',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='apps.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='price',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='apps.color', verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='price',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='apps.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='price',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='apps.size', verbose_name='Size'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='apps.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='apps.discount', verbose_name='Discount'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='product_images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='apps.price', verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='apps.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='size',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Slug'),
        ),
    ]