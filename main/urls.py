from django.urls import path, re_path

from . import views
from .feeds import LatestPostsFeed


from .views import IndexTemplateView, PostListView, ContactCreateView, PostDetailView, MatchesListView, VideoListView, \
    CommentCreateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('news/', PostListView.as_view(), name='news'),
    path('matches/', MatchesListView.as_view(), name='matches'),
    path('videos/', VideoListView.as_view(), name='videos'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('RSSfeed/', LatestPostsFeed(), name='post_feed'),
    path('<slug:post_slug>/', PostDetailView.as_view(), name='news_post'),
]