# Generated by Django 4.2.2 on 2023-06-07 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sims', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField()),
                ('item_id', models.CharField(max_length=15)),
                ('client', models.CharField(max_length=70)),
                ('product', models.CharField(choices=[('chip-internacional-eua', 'USA'), ('chip-internacional-eua-e-canada', 'USA e CANADA'), ('chip-internacional-europa', 'EUROPA'), ('chip-internacional-global', 'GLOBAL PREMIUM')], max_length=35)),
                ('data_day', models.CharField(choices=[('500mb-dia', '500GB'), ('1gb', '1GB'), ('2gb', '2GB'), ('ilimitado', 'Ilimitado')], max_length=15)),
                ('qty', models.IntegerField()),
                ('coupon', models.CharField(default=None, max_length=15)),
                ('days', models.IntegerField()),
                ('calls', models.BooleanField(default=False)),
                ('countries', models.BooleanField(default=False)),
                ('cell_mod', models.CharField(max_length=35)),
                ('ord_chip_nun', models.CharField(blank=True, default='-', max_length=25, null=True)),
                ('shipping', models.CharField(max_length=35)),
                ('order_date', models.DateTimeField()),
                ('activation_date', models.DateField()),
                ('order_status', models.CharField(choices=[('AT', 'Ativado'), ('CC', 'Cancelado'), ('RB', 'Reembolsado'), ('RP', 'Reprocessar'), ('PR', 'Processando')], default='PR', max_length=20)),
                ('condition', models.CharField(default='novo-sim', max_length=15)),
                ('notes', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_sim', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sims.sims')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'db_table': 'orders',
                'ordering': ['order_id'],
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='note', to='orders.orders')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Nota',
                'verbose_name_plural': 'Notas',
                'db_table': 'notes',
                'ordering': ['id_pedido'],
            },
        ),
    ]