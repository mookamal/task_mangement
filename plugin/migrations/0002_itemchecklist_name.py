# Generated by Django 4.2.5 on 2023-10-03 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemchecklist',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
