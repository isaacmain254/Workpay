from django.contrib import admin
from .models import Profile, Project, Bio, Skill

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'profile_image']
    raw_id_fields = ['user']

admin.site.register(Project)
admin.site.register(Bio)
admin.site.register(Skill)