from django.contrib import admin
from Book.models import BorrowBooks, BookDB

# Register your models here.
# admin.site.register(BorrowBooks)

@admin.register(BorrowBooks)
class BorrowBooksAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ('b_name', 'stu_name', 'stu_phone', 'stu_qq',)
    # fieldsets = (
    #     ['Main', {
    #         'fields': ('b_name', 'stu_name'),
    #     }],
    #     ['Advance', {
    #         'classes': ('collapse',),  # CSS
    #         'fields': ('stu_id',),
    #     }]
    # )
    search_fields = ('stu_name', 'b_name')

@admin.register(BookDB)
class BookDBAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ('b_name', 'b_img', 'b_status',)
    search_fields = ('b_name', 'b_status')