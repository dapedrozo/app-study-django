# Generated by Django 4.0.3 on 2022-04-03 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
