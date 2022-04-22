from django.db import models


class Note(models.Model):
    body = models.TextField(
        null=True,
        blank=True,
    )
    updated = models.DateTimeField(
        auto_now=True,  # Updated on each save
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.body[:50]