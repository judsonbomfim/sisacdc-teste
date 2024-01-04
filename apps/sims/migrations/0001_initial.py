# Generated by Django 4.2.2 on 2023-06-07 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sims',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sim', models.CharField(max_length=20)),
                ('link', models.URLField(blank=True, null=True)),
                ('type_sim', models.CharField(choices=[('sim', 'SIM (Físico)'), ('esim', 'eSIM (Virtual)')], max_length=20)),
                ('operator', models.CharField(choices=[('TM', 'T-Mobile'), ('CM', 'China Mobile'), ('TC', 'Telcom')], max_length=20)),
                ('sim_status', models.CharField(choices=[('DS', 'Disponível'), ('AT', 'Ativado'), ('CC', 'Cancelado')], default='DS', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Sim',
                'verbose_name_plural': 'Sims',
                'db_table': 'sims',
                'ordering': ['id'],
            },
        ),
    ]