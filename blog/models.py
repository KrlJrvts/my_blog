from django.utils import timezone
from django.db import models


# Create your models here.

class BlogPost(models.Model):
    LENGTH = 128
    PARAGRAPH_LENGTH = 1024

    title = models.CharField(null=False, blank=False, max_length=LENGTH, db_index=True, default='Title')
    paragraph = models.TextField(null=False, blank=False, max_length=PARAGRAPH_LENGTH)
    created_at = models.DateTimeField(default=timezone.now)
    author_name = models.CharField(null=False, blank=False, max_length=LENGTH, db_index=True, default='Anonymous')

    def __str__(self):
        return f'{self.title} - {self.author_name}'
