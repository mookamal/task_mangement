# Generated by Django 4.2.5 on 2023-09-16 10:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='team',
            field=models.ManyToManyField(related_name='team_board', to=settings.AUTH_USER_MODEL),
        ),
    ]