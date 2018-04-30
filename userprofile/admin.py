from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Profile

admin.site.unregister(User)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Profile'
    fk_name = 'user'


@admin.register(User)
class CustomUser(UserAdmin):
    inlines = (ProfileInline,)
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('profile.profile_image',)}),
    # )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)
