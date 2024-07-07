from django.contrib import admin
from . models import Fixture,Player,News
# Register your models here.

admin.site.register(Fixture)
admin.site.register(Player)
admin.site.register(News)