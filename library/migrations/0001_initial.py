# Generated by Django 3.2 on 2023-01-15 16:36

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.SlugField(null=True)),
                ('theme', models.CharField(blank=True, choices=[('architecture', 'ARCHITECTURE'), ('city', 'CITY'), ('classic', 'CLASSIC'), ('creator', 'CREATOR'), ('friends', 'FRIENDS'), ('ideas', 'IDEAS'), ('art', 'ART'), ('education', 'EDUCATION'), ('mario', 'MARIO'), ('spider-man', 'SPIDER_MAN')], max_length=12)),
                ('description', models.TextField()),
                ('done', models.BooleanField(default=False)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_sets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
