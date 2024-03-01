from django.contrib import admin

from .models import Collect, Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("money", "date_time_payment", "donating", "collect")


class CollectAdmin(admin.ModelAdmin):
    list_display = (
        "occasion",
        "author",
        "name",
        "description",
        "purpose",
        # "current_money",
        # "count_people",
        "logo",
        "date_time_collect",
    )


admin.site.register(Collect, CollectAdmin)
admin.site.register(Payment, PaymentAdmin)
