# Generated by Django 3.0.4 on 2020-03-25 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0006_auto_20200325_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fish',
            old_name='fish_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='fish_name',
            new_name='fish',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='cost_per_fish',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='fish_size',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='Orders.Order'),
        ),
    ]
