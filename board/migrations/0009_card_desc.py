# Generated by Django 4.2.5 on 2023-10-02 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='desc',
            field=models.TextField(default='add description'),
        ),
    ]
