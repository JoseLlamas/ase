# Generated by Django 3.0.5 on 2020-06-05 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_hostvirtual_activo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servidor',
            name='valido',
        ),
        migrations.AddField(
            model_name='servidor',
            name='activo',
            field=models.BooleanField(db_column='activo', default=True),
        ),
    ]
