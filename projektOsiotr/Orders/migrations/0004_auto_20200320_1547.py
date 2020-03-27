# Generated by Django 3.0.4 on 2020-03-20 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0003_auto_20200320_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('cost_per_fish', models.DecimalField(decimal_places=2, max_digits=8)),
                ('fish', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Orders.Fish')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Orders.Order')),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='Orders.OrderItem', to='Orders.Fish'),
        ),
    ]
