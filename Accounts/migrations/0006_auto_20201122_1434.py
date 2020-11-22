# Generated by Django 3.1.3 on 2020-11-22 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_auto_20201122_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wish_movie', to=settings.AUTH_USER_MODEL),
        ),
    ]
