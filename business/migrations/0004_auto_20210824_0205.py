# Generated by Django 3.2.4 on 2021-08-24 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_auto_20210824_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
