# Generated by Django 3.0.7 on 2020-06-16 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodfinder', '0011_auto_20200616_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodnutriment',
            name='nutriment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='food_nutriment_set', to='foodfinder.Nutriment'),
        ),
    ]
