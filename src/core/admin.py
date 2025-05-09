from django.contrib import admin

# Register your models here.
class TimeStampModelAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'created', 'modified']