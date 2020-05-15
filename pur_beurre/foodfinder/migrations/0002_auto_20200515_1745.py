# Generated by Django 3.0.6 on 2020-05-15 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foodfinder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='search_algorythm',
            field=models.CharField(choices=[('BY_FAT', 'By Fat'), ('BY_SALT', 'By Salt'), ('BY_NUTRIMENTS', 'By Nutriments'), ('BY_CATEGORY', 'By Category')], default='BY_FAT', max_length=63),
        ),
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
