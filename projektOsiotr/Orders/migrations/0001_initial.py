# Generated by Django 3.0.4 on 2020-03-20 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FishType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fish_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latin_name', models.CharField(max_length=100)),
                ('size', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('description', models.TextField(default='Opis', max_length=1000)),
                ('stock', models.IntegerField()),
                ('fish_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Orders.FishType')),
            ],
        ),
    ]
