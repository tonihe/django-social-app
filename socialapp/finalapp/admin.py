from django.contrib import admin
from .models import Post, UserProfile, Comment, ThreadModel, MessageModel

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(ThreadModel)
admin.site.register(MessageModel)