# Generated by Django 5.0.1 on 2024-02-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0008_remove_product_currency_ids'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discount',
            new_name='discount_id',
        ),
        migrations.AddField(
            model_name='product',
            name='currency_ids',
            field=models.ManyToManyField(related_name='products', to='apps.currency'),
        ),
    ]
