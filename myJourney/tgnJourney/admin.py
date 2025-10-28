from django.contrib import admin
from .models import LearningJourney, AboutMe

# Register your models here.


# Register your models to show them in the admin panel
@admin.register(LearningJourney)
class LearningJourneyAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_started', 'last_updated')
    search_fields = ('title', 'description')
    list_filter = ('date_started',)

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')