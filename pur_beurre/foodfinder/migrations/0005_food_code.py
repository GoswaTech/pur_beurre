# Generated by Django 3.0.7 on 2020-06-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodfinder', '0004_auto_20200612_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='code',
            field=models.CharField(default=None, max_length=15, unique=True),
            preserve_default=False,
        ),
    ]
