# Generated by Django 3.2.4 on 2021-08-18 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0005_auto_20210818_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.group'),
        ),
    ]
