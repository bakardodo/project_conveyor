from django.contrib import admin

# Register your models here.
from project_conveyor.conveyor_app.models import UCFLbodies, UserPurchases


@admin.register(UCFLbodies)
class UCFLbodiesAdmin(admin.ModelAdmin):
    pass

@admin.register(UserPurchases)
class UserPurchasesAdmin(admin.ModelAdmin):
    pass

