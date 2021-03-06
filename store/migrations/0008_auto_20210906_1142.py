# Generated by Django 3.2.4 on 2021-09-06 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210904_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='generic',
            field=models.ForeignKey(blank=True, help_text='Paracetamol > syrup paracetamol > tablet', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='generics', to='store.generic'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('name', 'unit')},
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('name', 'unit')},
        ),
    ]
