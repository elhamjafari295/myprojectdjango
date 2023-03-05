from django.contrib import admin
from .models import Article,Category,IPAddress

admin.site.disable_action('delete_selected')

def make_published(modeladmin, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "منتشر شد."
        else:
            message_bit = "منتشر شدند"
        modeladmin.message_user(request, "{} مقاله {}".format(rows_updated,message_bit))

make_published.short_description = "انتشار مقالات انتخاب شده"  

def make_draft(modeladmin, request, queryset):
        rows_updated = queryset.update(status='d')
        if rows_updated == 1:
            message_bit = "مپیش نویس شد"
        else:
            message_bit = "پیش نویس شدند"
        modeladmin.message_user(request, "{} مقاله {}".format(rows_updated,message_bit))
make_draft.short_description = "اپیش نویس شدن مقالات انتخاب شده"    
class CategoryAdmin(admin.ModelAdmin):
	list_display=('position','title','slug', 'parent', 'status')
	list_filter=(['status'])
	search_fields=('title','slug')
	prepopulated_fields={'slug':('title',)}
	
# Register your models here.
admin.site.register(Category,CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','thumbnail_tag','slug','author','jpublish','is_special','status','category_to_str')
	list_filter=('publish','status','author')
	search_fields=('title','description')
	prepopulated_fields={'slug':('title',)}
	ordering=['status','publish']
	actions = [make_published, make_draft]

	

# Register your models here.
admin.site.register(Article,ArticleAdmin)
admin.site.register(IPAddress)
