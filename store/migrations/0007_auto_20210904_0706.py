# Generated by Django 3.2.4 on 2021-09-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_auto_20210827_0114'),
        ('store', '0006_auto_20210904_0652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='supplier',
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ManyToManyField(blank=True, related_name='suppliers', to='business.Supplier'),
        ),
    ]
