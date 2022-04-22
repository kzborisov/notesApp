from django.contrib import admin

from notesApp.api.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('body', 'updated', 'created_at')
