from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.
from .models import Subject, Department, Rating, Note

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
    list_display = ('name','code', 'semester',)
    list_filter = ('semester',)
    readonly_fields = ('sub_image',)

    # fieldsets = (
    #     (None, {'fields': ('name','sub_image', 'image'),}),
    # )


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass
