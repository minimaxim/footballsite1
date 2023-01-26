# Generated by Django 4.1.4 on 2023-01-25 19:09

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='name')),
                ('url', models.CharField(blank=True, max_length=256, null=True, verbose_name='video url')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('is_published', models.BooleanField(default=True, verbose_name='published')),
                ('image', models.ImageField(null=True, upload_to='video_image/', verbose_name='image')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
                'db_table': 'main_videos',
                'ordering': ['date_created'],
            },
        ),
        migrations.AlterModelOptions(
            name='lastmatch',
            options={'verbose_name': 'last match', 'verbose_name_plural': 'last matches'},
        ),
        migrations.AlterModelOptions(
            name='nearmatch',
            options={'verbose_name': 'near match', 'verbose_name_plural': 'near matches'},
        ),
        migrations.AlterModelOptions(
            name='upcomingmatch',
            options={'verbose_name': 'upcoming match', 'verbose_name_plural': 'upcoming matches'},
        ),
        migrations.RemoveField(
            model_name='arena',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='tournaments',
            name='slug',
        ),
        migrations.AddField(
            model_name='lastmatch',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='published'),
        ),
        migrations.AddField(
            model_name='lastmatch',
            name='team_one_image',
            field=models.ImageField(null=True, upload_to='teams_image/', verbose_name='Team one emblema'),
        ),
        migrations.AddField(
            model_name='lastmatch',
            name='team_two_image',
            field=models.ImageField(null=True, upload_to='teams_image/', verbose_name='Team two emblema'),
        ),
        migrations.AddField(
            model_name='nearmatch',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='published'),
        ),
        migrations.AddField(
            model_name='nearmatch',
            name='near_team_one_image',
            field=models.ImageField(null=True, upload_to='teams_image/', verbose_name='Team one emblema'),
        ),
        migrations.AddField(
            model_name='nearmatch',
            name='near_team_two_image',
            field=models.ImageField(null=True, upload_to='teams_image/', verbose_name='Team two emblema'),
        ),
        migrations.AddField(
            model_name='newpost',
            name='likes',
            field=models.ManyToManyField(related_name='newpost_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='upcomingmatch',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='published'),
        ),
        migrations.AddField(
            model_name='upcomingmatch',
            name='up_team_one_image',
            field=models.ImageField(null=True, upload_to='teams_image/', verbose_name='Team one emblema'),
        ),
        migrations.AddField(
            model_name='upcomingmatch',
            name='up_team_two_image',
            field=models.ImageField(null=True, upload_to='teams_image/', verbose_name='Team two emblema'),
        ),
        migrations.AlterField(
            model_name='newpost',
            name='image',
            field=models.ImageField(null=True, upload_to='news_image/', verbose_name='image'),
        ),
    ]
