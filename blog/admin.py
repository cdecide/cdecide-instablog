from django.contrib import admin

from .models import Post, Comment, Tag, Category

class PostAdmin(admin.ModelAdmin):
	list_display = ('pk', 'title', 'created_at', )
	list_display_links = ('pk', 'title', )
	ordering = ('-id', )
	search_fields = ('title', 'content', )
	list_filter = ('category', 'created_at', )

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)