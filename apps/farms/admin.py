from django.contrib import admin

from apps.farms.models import Company, Product, Success_story, About_us,\
    Application, Contact, Companies


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'picture']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'picture']


@admin.register(Success_story)
class Success_storyAdmin(admin.ModelAdmin):
    list_display = ['feedback', 'picture']


@admin.register(About_us)
class About_usAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'picture']


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'message', 'country', 'mail', 'whatsapp',
                    'telegram', 'created_at']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'mail', 'phone_one', 'phone_two',
                    'whatsapp_number', 'instagram', 'facebook', 'youtube',
                    'gmail']


@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ['name']