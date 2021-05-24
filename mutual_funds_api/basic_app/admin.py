from django.contrib import admin
from basic_app.models import MutualFundsCode, MutualFundsScheme
# Register your models here.
@admin.register(MutualFundsCode)
class MutualFundsCodeAdmin(admin.ModelAdmin):
    list_display = ('code','description')

@admin.register(MutualFundsScheme)
class MutualFundsSchemeAdmin(admin.ModelAdmin):
    list_display = ('scheme_code','scheme_category', 'scheme_type', 'fund_house')