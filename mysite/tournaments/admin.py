from django.contrib import admin

from .models import tournament,team,pool,match

admin.site.register(tournament)
admin.site.register(team)
admin.site.register(pool)
admin.site.register(match)