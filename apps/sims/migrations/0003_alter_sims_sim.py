# Generated by Django 4.2.2 on 2023-06-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0002_alter_sims_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sims',
            name='sim',
            field=models.CharField(max_length=25),
        ),
    ]