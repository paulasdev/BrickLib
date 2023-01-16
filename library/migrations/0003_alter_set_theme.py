# Generated by Django 3.2 on 2023-01-15 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_name_set_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='theme',
            field=models.CharField(blank=True, choices=[('Architecture', 'ARCHITECTURE'), ('City', 'CITY'), ('Classic', 'CLASSIC'), ('Creator', 'CREATOR'), ('Friends', 'FRIENDS'), ('Ideas', 'IDEAS'), ('Art', 'ART'), ('Education', 'EDUCATION'), ('Mario', 'MARIO'), ('Spider-man', 'SPIDER_MAN')], max_length=12),
        ),
    ]
