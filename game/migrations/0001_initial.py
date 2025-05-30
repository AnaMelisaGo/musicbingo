# Generated by Django 5.2 on 2025-04-27 19:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played_on', models.DateTimeField(auto_now_add=True)),
                ('playlist', models.CharField(max_length=255)),
                ('game_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-played_on'],
            },
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('prize', models.CharField(max_length=255)),
                ('winning_numbers', models.JSONField(default=list)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='game.game')),
            ],
        ),
    ]
