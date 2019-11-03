from django.contrib import admin

from matches.models import Match, Delivery


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Match._meta.fields]


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Delivery._meta.fields]
