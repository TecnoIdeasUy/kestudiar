# Generated by Django 3.0.4 on 2020-04-03 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_curso_locacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='locacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Locacion'),
        ),
    ]
