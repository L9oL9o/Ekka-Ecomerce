# Generated by Django 5.0.1 on 2024-02-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_currency_alter_price_count_alter_price_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency_ids',
            field=models.ManyToManyField(related_name='products', to='apps.currency'),
        ),
    ]