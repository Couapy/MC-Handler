# Generated by Django 3.0.4 on 2020-07-08 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_auto_20200708_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servershare',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur'),
        ),
    ]
