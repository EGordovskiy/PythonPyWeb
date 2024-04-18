from django.contrib import admin
from .models import Author, AuthorProfile, Entry, Tag
# from rest_framework.authtoken.models import Token

admin.site.register(Author)
admin.site.register(AuthorProfile)
admin.site.register(Entry)
admin.site.register(Tag)
# admin.site.register(Token)
