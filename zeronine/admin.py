from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_code', 'name', 'slug']
    prepopulated_fields = {'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display=['product_code',
                  'name',
                  'username',
                  'slug',
                  'image',
                  'category_code',
                  'benefit',
                  'detail',
                  'target_price',
                  'start_date',
                  'due_date',
                  'created_at',
                  'kakao_link']

    prepopulated_fields = {'slug': ('name',)}

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'post_code',
        'username',
        'title',
        'content',
        'register_date'
    )

    search_fields = ['title']

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'comment_code',
        'post_code',
        'username',
        'content',
        'register_date'
    )

    search_fields = ['content']

class ZzimAdmin(admin.ModelAdmin):
    list_display = (
        'zzim_code',
        'username',
        'product_code',
    )

class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'photo_code',
        'product_code',
        'photo',
    )

class OptionAdmin(admin.ModelAdmin):
    list_display = (
        'option_code',
        'name',
        'product_code',
    )

class ValueAdmin(admin.ModelAdmin):
    list_display = (
        'value_code',
        'option_code',
        'product_code',
        'name',
        'extra_cost',
    )

class DesignatedAdmin(admin.ModelAdmin):
    list_display = (
        'designated_code',
        'product_code',
        'price',
        'rep_price',
    )

class ElementAdmin(admin.ModelAdmin):
    list_display = (
        'element_code',
        'designated_code',
        'value_code',
    )

class JoinAdmin(admin.ModelAdmin):
    list_display = (
        'join_code',
        'username',
        'product_code',
        'part_date',
    )

class JoinDetailAdmin(admin.ModelAdmin):
    list_display = (
        'joindetail_code',
        'join_code',
        'value_code',
        'designated_code',
        'quantity',
        'price',
    )

admin.site.register(Member)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Zzim, ZzimAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Value, ValueAdmin)
admin.site.register(Designated, DesignatedAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(Join, JoinAdmin)
admin.site.register(JoinDetail, JoinDetailAdmin)
