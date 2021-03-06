# Generated by Django 3.1 on 2020-08-12 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0002_molecule_inchikey'),
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('symbol', models.CharField(max_length=3)),
                ('atomic_mass', models.CharField(max_length=200)),
                ('am_unit', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='molecule',
            old_name='mw_units',
            new_name='mw_unit',
        ),
    ]
