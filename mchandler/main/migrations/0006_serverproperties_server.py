# Generated by Django 3.0.4 on 2020-05-20 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_serverproperties'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverproperties',
            name='server',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Server'),
        ),
    ]
