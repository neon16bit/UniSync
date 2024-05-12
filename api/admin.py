from django.contrib import admin
from .models import ClassSlot, ClassSlots,Instructor, Room, Course, Curriculum, CourseInstructor, RoomSchedule, ClassSchedule,  GenerateSchedule

admin.site.register(Room)
admin.site.register(Curriculum)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(ClassSlot)
admin.site.register(ClassSlots)
admin.site.register(ClassSchedule)
admin.site.register(CourseInstructor)
admin.site.register(RoomSchedule)
admin.site.register(GenerateSchedule)
