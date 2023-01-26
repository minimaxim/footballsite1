from django.contrib import admin

from .models import Category, NewPost, Contact, LastMatch, Tournaments, Arena, NearMatch, UpcomingMatch, Videos, \
    Comment


@admin.action(description='Publish')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Unpublish')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions = (make_unpublished, make_published)
    list_display = ('id', 'name', 'is_published')
    list_editable = ('name',)
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(NewPost)
class NewPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    search_help_text = ('SEARCH')
    readonly_fields = ('date_created',)
    date_hierarchy = 'date_created'
    ordering = ('date_created', 'name')
    list_display = ('name', 'full_name', 'date')
    list_filter = ('is_published', 'category')

    fieldsets = (
        (
            'Main',
            {
                'fields': ('name', 'descr', 'category')
            }
        ),
        (
            'Secondary tools',
            {
                'fields': ('date_created', 'author', 'slug', 'image', 'back_image')
            }
        )
    )


@admin.register(Tournaments)
class TournamentsAdmin(admin.ModelAdmin):
    actions = (make_unpublished, make_published)
    list_display = ('id', 'name', 'is_published')
    list_editable = ('name',)
    list_filter = ('is_published',)


@admin.register(Arena)
class ArenaAdmin(admin.ModelAdmin):
    actions = (make_unpublished, make_published)
    list_display = ('id', 'name', 'is_published')
    list_editable = ('name',)
    list_filter = ('is_published',)


@admin.register(LastMatch)
class LastMatchAdmin(admin.ModelAdmin):
    actions = (make_unpublished, make_published)
    list_display = ('tournament', 'match_date', 'team_one', 'team_two', 'arena', 'is_published')
    list_filter = ('match_date', 'arena', 'tournament', 'is_published')
    fieldsets = (
        (
            'Main videos',
            {
                'fields': ('tournament', 'match_date', 'team_one', 'team_one_image', 'team_two', 'team_two_image',
                           'arena')
            }
        ),
        (
            'Goals',
            {
                'fields': ('goals_team_one', 'goals_team_two')
            }
        ),
        (
            'Players with goals',
            {
                'fields': ('players_team_one', 'players_team_two')
            }
        )
    )


@admin.register(NearMatch)
class NearMatchAdmin(admin.ModelAdmin):
    actions = (make_unpublished, make_published)
    list_display = ('tournament', 'match_date', 'near_match_team_one',
                    'near_match_team_two', 'arena', 'is_published')
    list_filter = ('match_date', 'arena', 'tournament', 'is_published')
    fieldsets = (
        (
            'Main videos',
            {
                'fields': ('tournament', 'match_date', 'near_match_team_one', 'near_team_one_image',
                           'near_match_team_two', 'near_team_two_image', 'arena')
            }
        ),
    )


@admin.register(UpcomingMatch)
class UpcomingMatchAdmin(admin.ModelAdmin):
    actions = (make_unpublished, make_published)
    list_display = ('tournament', 'match_date', 'upcoming_match_team_one', 'upcoming_match_team_two',
                    'is_published', 'arena')
    list_filter = ('match_date', 'arena', 'tournament', 'is_published')


@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    actions = (make_unpublished, make_published)
    list_display = ('name',)
    list_filter = ('date_created', 'is_published')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']
