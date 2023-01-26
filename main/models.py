from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='category'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='published'
    )
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Ip(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class NewPost(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='name'
    )
    descr = models.TextField(verbose_name='description')
    is_published = models.BooleanField(
        default=True,
        verbose_name='published'
    )
    date_created = models.DateTimeField(
        default=now,
        verbose_name='date created'
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='author'
    )
    image = models.ImageField(
        upload_to='news_image/',
        verbose_name='image',
        null=True
    )
    back_image = models.ImageField(
        upload_to='news_back_image/',
        verbose_name='back_image',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='category'
    )
    show_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news_post', kwargs={'post_slug': self.slug})

    @property
    def date(self) -> str:
        return self.date_created

    @property
    def full_name(self):
        return self.author.first_name + ' ' + self.author.last_name


    class Meta:
        db_table = 'main_posts'
        verbose_name = 'news'
        verbose_name_plural = 'news'
        ordering = ['date_created']


class Tournaments(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='tournament'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='published'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_tournaments'
        verbose_name = 'tournament'
        verbose_name_plural = 'tournaments'


class Arena(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='arena'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='published'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_arens'
        verbose_name = 'arena'
        verbose_name_plural = 'arens'


class LastMatch(models.Model):
    team_one = models.CharField(
        max_length=32,
        verbose_name='name team 1'
    )
    team_one_image = models.ImageField(
        upload_to='teams_image/',
        verbose_name='Team one emblema',
        null=True
    )
    goals_team_one = models.CharField(
        max_length=2,
        verbose_name='goals team 1'
    )
    players_team_one = models.CharField(
        max_length=256,
        verbose_name='goleadors team 1'
    )
    team_two = models.CharField(
        max_length=32,
        verbose_name='name team 2'
    )
    team_two_image = models.ImageField(
        upload_to='teams_image/',
        verbose_name='Team two emblema',
        null=True
    )
    goals_team_two = models.CharField(
        max_length=2,
        verbose_name='goals team 2'
    )
    players_team_two = models.CharField(
        max_length=256,
        verbose_name='goleadors team 2'
    )
    tournament = models.ForeignKey(
        'Tournaments',
        on_delete=models.CASCADE,
        verbose_name='tournament'
    )
    match_date = models.DateTimeField(
        default=now,
        verbose_name='match day'
    )
    arena = models.ForeignKey(
        'Arena',
        on_delete=models.CASCADE,
        verbose_name='arena'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='published'
    )

    def __str__(self):
        return 'Last match'


    class Meta:
        db_table = 'main_matches'
        verbose_name = 'last match'
        verbose_name_plural = 'last matches'


class NearMatch(models.Model):
    near_match_team_one = models.CharField(
        max_length=32,
        verbose_name='near match name team 1'
    )
    near_match_team_two = models.CharField(
        max_length=32,
        verbose_name='near match name team 2'
    )
    near_team_one_image = models.ImageField(
        upload_to='teams_image/',
        verbose_name='Team one emblema',
        null=True
    )
    near_team_two_image = models.ImageField(
        upload_to='teams_image/',
        verbose_name='Team two emblema',
        null=True
    )
    tournament = models.ForeignKey(
        'Tournaments',
        on_delete=models.CASCADE,
        verbose_name='tournament'
    )
    match_date = models.DateTimeField(
        default=now,
        verbose_name='match day'
    )
    arena = models.ForeignKey(
        'Arena',
        on_delete=models.CASCADE,
        verbose_name='arena'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='published'
    )

    def __str__(self):
        return 'Near match'


    class Meta:
        db_table = 'main_nearmatches'
        verbose_name = 'near match'
        verbose_name_plural = 'near matches'


class UpcomingMatch(models.Model):
    upcoming_match_team_one = models.CharField(
        max_length=32,
        default=None,
        verbose_name='upcoming match name team 1'
    )
    upcoming_match_team_two = models.CharField(
        max_length=32,
        default=None,
        verbose_name='upcoming match name team 2'
    )
    up_team_one_image = models.ImageField(
        upload_to='teams_image/',
        verbose_name='Team one emblema',
        null=True
    )
    up_team_two_image = models.ImageField(
        upload_to='teams_image/',
        verbose_name='Team two emblema',
        null=True
    )
    tournament = models.ForeignKey(
        'Tournaments',
        on_delete=models.CASCADE,
        verbose_name='tournament'
    )
    match_date = models.DateTimeField(
        default=now,
        verbose_name='match day'
    )
    arena = models.ForeignKey(
        'Arena',
        on_delete=models.CASCADE,
        verbose_name='arena'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='published'
    )

    def __str__(self):
        return 'Upcoming match'


    class Meta:
        db_table = 'main_upmatches'
        verbose_name = 'upcoming match'
        verbose_name_plural = 'upcoming matches'


class Contact(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='name'
    )
    email = models.EmailField(
        verbose_name='email'
    )
    message = models.CharField(
        max_length=1024,
        verbose_name='message'
    )
    date_created = models.DateTimeField(
        default=now,
        verbose_name='date created'
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'main_contacts'
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ['date_created']


class Videos(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='name'
    )
    url = models.CharField(
        verbose_name='video url',
        max_length=256,
        null=True,
        blank=True
    )
    date_created = models.DateTimeField(
        default=now,
        verbose_name='date created'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='published'
    )
    image = models.ImageField(
        upload_to='video_image/',
        verbose_name='image',
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_videos'
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        ordering = ['date_created']


class Comment(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='name'
    )
    email = models.EmailField(
        verbose_name='email'
    )
    message = models.CharField(
        max_length=1024,
        verbose_name='message'
    )
    date_created = models.DateTimeField(
        default=now,
        verbose_name='date created'
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'main_comments'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ['date_created']


