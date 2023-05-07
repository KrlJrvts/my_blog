from django.db import models


# Create your models here.
class BlogPost(models.Model):
    """ A model that represents a single blogpost"""

    title = models.CharField(null=False, blank=False, max_length=128)
    paragraph = models.TextField(null=False, blank=False, max_length=1024)
    created = models.DateTimeField(null=False, blank=False)
    author = models.CharField(null=False, blank=False, max_length=128)


"""
class BlogPost(models.Model):
    LENGTH = 128
    PARAGRAPH_LENGTH = 1024

    title_text = models.CharField(null=False, blank=False, max_length=LENGTH, db_index=True)
    paragraph = models.TextField(null=False, blank=False, max_length=PARAGRAPH_LENGTH)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    author_name = models.CharField(null=False, blank=False, max_length=LENGTH, db_index=True)
"""