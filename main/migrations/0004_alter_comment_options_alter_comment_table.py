# Generated by Django 4.1.4 on 2023-01-25 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',), 'verbose_name': 'comment', 'verbose_name_plural': 'comments'},
        ),
        migrations.AlterModelTable(
            name='comment',
            table='main_comments',
        ),
    ]