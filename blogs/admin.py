from django.contrib import admin
from blogs.models import *

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass
# your_app/admin.py


class SubscriberAdmin(admin.ModelAdmin):
    pass

class NewsletterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)