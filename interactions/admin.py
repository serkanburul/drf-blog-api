from django.contrib import admin
from interactions.models import Like, Dislike, Favorite

admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Favorite)
