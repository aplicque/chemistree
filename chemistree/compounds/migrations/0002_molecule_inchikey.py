# Generated by Django 3.1 on 2020-08-09 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='molecule',
            name='inchikey',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
