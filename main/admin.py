from django.contrib import admin
from .models import Gallery, Faculty,Event, Newsletter, placements,studentachi,teacherachi,testmonials,Enquiry,contactus
# Register your models here.


admin.site.register(Gallery)
admin.site.register(Faculty)
admin.site.register(Event)
admin.site.register(Newsletter)
admin.site.register(placements)
admin.site.register(teacherachi)
admin.site.register(studentachi)
admin.site.register(testmonials)
admin.site.register(contactus)
admin.site.register(Enquiry)