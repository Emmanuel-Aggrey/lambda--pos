# Generated by Django 3.2.4 on 2021-08-24 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20210824_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
