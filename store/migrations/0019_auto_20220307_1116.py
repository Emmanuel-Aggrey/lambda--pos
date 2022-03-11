# Generated by Django 3.2.4 on 2022-03-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_alter_product_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='item',
            name='serial_number',
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]