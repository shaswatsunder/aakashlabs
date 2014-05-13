from django.contrib import admin
from forum.models import UserProfile, Category, Post, Reply

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Reply)
