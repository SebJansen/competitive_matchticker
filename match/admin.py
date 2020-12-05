from django.contrib import admin

from match.models import Player, MatchPlayer, Match, MatchOutcome


@admin.register(MatchOutcome)
class MatchOutcomeAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass


@admin.register(MatchPlayer)
class MatchPlayerAdmin(admin.ModelAdmin):
    pass


class MatchPlayerInline(admin.TabularInline):
    model = MatchPlayer
    extra = 0


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    inlines = [MatchPlayerInline]
