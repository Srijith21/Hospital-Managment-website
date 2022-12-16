from django.contrib import admin
from .models import Department,Doctor,Booking
# Register your models here.

admin.site.register(Department)
admin.site.register(Doctor)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name','booked_on','booking_date')
admin.site.register(Booking,BookingAdmin)