from django.contrib import admin
from .models import Room, Curriculum, Course, faculty_member

admin.site.register(Room)
admin.site.register(Curriculum)
admin.site.register(Course)
admin.site.register(faculty_member)
