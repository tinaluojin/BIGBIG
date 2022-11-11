# Generated by Django 2.1.12 on 2022-11-11 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.IntegerField()),
                ('updated_at', models.IntegerField()),
                ('format_created_at', models.DateTimeField(auto_now=True)),
                ('format_updated_at', models.DateTimeField(auto_now_add=True)),
                ('adress', models.CharField(default='cd', max_length=200)),
                ('phone', models.CharField(default='123456789', max_length=20)),
                ('value', models.DecimalField(decimal_places=5, default=0, max_digits=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to='users.Users')),
            ],
            options={
                'verbose_name': 'orders',
                'verbose_name_plural': 'orders',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrdersGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.IntegerField()),
                ('updated_at', models.IntegerField()),
                ('format_created_at', models.DateTimeField(auto_now=True)),
                ('format_updated_at', models.DateTimeField(auto_now_add=True)),
                ('num', models.IntegerField(default=0)),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='good_ordersGoods', to='goods.Goods')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ordersGoods', to='orders.Orders')),
            ],
            options={
                'verbose_name': 'ordersGoods',
                'verbose_name_plural': 'ordersGoods',
                'db_table': 'ordersGoods',
            },
        ),
    ]