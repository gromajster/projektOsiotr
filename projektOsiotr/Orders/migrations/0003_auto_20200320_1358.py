# Generated by Django 3.0.4 on 2020-03-20 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_auto_20200320_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fishtype',
            old_name='fish_type_name',
            new_name='name',
        ),
    ]
