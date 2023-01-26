from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import ContactForm, CommentForm
from .models import NewPost, Contact, LastMatch, NearMatch, UpcomingMatch, Videos, Comment, Ip


class BaseMixin:
    context = {
        'twitter': 'https://twitter.com',
        'facebook': 'https://facebook.com',
        'instagram': 'https://instagram.com',
        'youtube':'https://youtube.com'
    }


class IndexTemplateView(BaseMixin, ListView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data()
        context['news'] = NewPost.objects.all()
        context['matches'] = LastMatch.objects.all()
        context['near_match'] = NearMatch.objects.all()
        context['videos'] = Videos.objects.all()
        context.update(self.context)
        return context

    def get_queryset(self):
        return [
            NewPost.objects.filter(is_published=True),
            LastMatch.objects.filter(is_published=True),
            NearMatch.objects.filter(is_published=True),
            Videos.objects.filter(is_published=True)
        ]


class PostListView(BaseMixin, ListView):
    template_name = 'news/blog.html'
    context_object_name = 'news'
    model = NewPost

    def get_queryset(self):
        return NewPost.objects.filter(is_published=True)


class PostDetailView(BaseMixin, DetailView):
    template_name = 'news/single.html'
    context_object_name = 'news_post'
    slug_url_kwarg = 'post_slug'
    model = NewPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = CommentForm()
        context.update(self.context)
        return context

    def get_object(self, queryset=None):
        self.object = super(PostDetailView, self).get_object()
        self.object.show_count += 1
        self.object.save()
        return self.object


class MatchesListView(BaseMixin, ListView):
    template_name = 'matches/matches.html'
    context_object_name = 'matches'
    model = LastMatch

    def get_context_data(self, **kwargs):
        context = super(MatchesListView, self).get_context_data()
        context['near_match'] = NearMatch.objects.all()
        context['up_match'] = UpcomingMatch.objects.all()
        context['video'] = Videos.objects.all()
        context.update(self.context)
        return context


class VideoListView(BaseMixin, ListView):
    template_name = 'videos/video.html'
    context_object_name = 'videos'
    model = Videos

    def get_context_data(self, **kwargs):
        context = super(VideoListView, self).get_context_data()
        context['news'] = NewPost.objects.all()
        context.update(self.context)
        return context


class ContactCreateView(BaseMixin, CreateView):
    template_name = 'contact/contact.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


class CommentCreateView(BaseMixin, CreateView):
    template_name = 'comment_form/form.html'
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')  # В REMOTE_ADDR значение айпи пользователя
    return ip





