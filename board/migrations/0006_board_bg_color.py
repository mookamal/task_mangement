# Generated by Django 4.2.5 on 2023-09-17 07:56

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_remove_board_bg_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='bg_color',
            field=colorfield.fields.ColorField(default='#fff', image_field=None, max_length=25, samples=None),
        ),
    ]