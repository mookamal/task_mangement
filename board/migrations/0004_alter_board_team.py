# Generated by Django 4.2.5 on 2023-09-16 11:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0003_board_created_at_board_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='team',
            field=models.ManyToManyField(blank=True, related_name='team_board', to=settings.AUTH_USER_MODEL),
        ),
    ]
