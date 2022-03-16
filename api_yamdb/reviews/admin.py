from django.contrib import admin
from .models import User, Category, Comment, Genre, Review, Title


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username',)
#         'username', 'email', 'role', 'bio', 'first_name', 'last_name'
#     )
#     search_fields = ('',)
#     list_filter = ('',)
#     empty_value_display = '-пусто-'


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     search_fields = ('',)
#     list_filter = ('',)
#     empty_value_display = '-пусто-'


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('text', 'author', 'pub_date')
#     # search_fields = ('',)
#     # list_filter = ('',)
#     empty_value_display = '-пусто-'


# class GenreAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     search_fields = ('',)
#     list_filter = ('',)
#     empty_value_display = '-пусто-'


# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('text', 'score', 'author', 'pub_date')
#     # search_fields = ('',)
#     # list_filter = ('',)
#     empty_value_display = '-пусто-'


# class TitleAdmin(admin.ModelAdmin):
#     list_display = ('name', 'year', 'category', 'genre', 'description')
#     search_fields = ('',)
#     list_filter = ('',)
#     empty_value_display = '-пусто-'


admin.site.register(User)  # UserAdmin)
admin.site.register(Category)  # CategoryAdmin)
admin.site.register(Comment)  # CommentAdmin)
admin.site.register(Genre)  # GenreAdmin)
admin.site.register(Review)  # ReviewAdmin)
admin.site.register(Title)  # TitleAdmin)
