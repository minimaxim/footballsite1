# Generated by Django 4.1.4 on 2023-01-26 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_comment_options_alter_comment_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
