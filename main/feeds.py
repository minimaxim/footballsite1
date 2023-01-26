from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import NewPost
from django.urls import reverse


class LatestPostsFeed(Feed):
    title = 'News'
    link = ''
    description = 'You can see all news here in RSS'

    def items(self):
        return NewPost.objects.order_by('date_created')

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return truncatewords(item.descr, 30)

    def item_link(self, item):
        return reverse('news_post', args={item.pk})