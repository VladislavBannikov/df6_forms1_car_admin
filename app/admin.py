from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ["brand", "model", "review_count"]
    pass


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm

    list_display = ["car", "title" ]
    search_fields = ("title",)
    list_filter = ("car",)
    # list_filter = ["review"]

admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
