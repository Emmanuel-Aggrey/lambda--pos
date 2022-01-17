# Generated by Django 3.2.4 on 2021-09-07 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20210906_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='generic',
            field=models.ForeignKey(help_text='Paracetamol > syrup paracetamol > tablet', on_delete=django.db.models.deletion.CASCADE, related_name='generics', to='store.generic'),
        ),
    ]