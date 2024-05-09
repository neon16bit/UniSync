from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib import messages
from .models import Curriculum, Course, Room, ClassSlot, ClassSlots, Instructor, RoomSchedule, CourseInstructor, ClassSchedule, GenerateSchedule

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def curriculum_list(request):
    curriculums = Curriculum.objects.all()
    return render(request, 'curriculum_list.html', {'curriculums': curriculums})

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

def faculty_member_list(request):
    faculty_members = Instructor.objects.all()
    return render(request, 'faculty_member_list.html', {'faculty_members': faculty_members}) 

@transaction.atomic
def generate_schedule(request):
    if request.method == 'POST':
        # Handle form submission
        curriculum_ids = request.POST.getlist('curriculum')
        if not curriculum_ids:
            messages.error(request, 'Please select at least one curriculum.')
            return redirect('generate_schedule')

        curriculums = Curriculum.objects.filter(pk__in=curriculum_ids)

        class_schedules = []
        for curriculum in curriculums:
            course_instructors = []
            for course in curriculum.courses.all():
                instructor_ids = request.POST.getlist(f'course_{course.pk}_instructors')
                if not instructor_ids:
                    messages.error(request, f'Please select at least one instructor for {course.course_code}.')
                    return redirect('generate_schedule')

                instructors = Instructor.objects.filter(pk__in=instructor_ids)
                course_instructor = CourseInstructor.objects.create(curriculum=curriculum, course=course)
                course_instructor.instructors.set(instructors)
                course_instructors.append(course_instructor)

            section_names = request.POST.getlist(f'curriculum_{curriculum.pk}_sections')
            room_ids = request.POST.getlist(f'curriculum_{curriculum.pk}_rooms')
            if not section_names or not room_ids:
                messages.error(request, f'Please provide section names and rooms for {curriculum.curriculum_semester}.')
                return redirect('generate_schedule')

            rooms = Room.objects.filter(pk__in=room_ids)

            room_schedules = []
            for i, section_name in enumerate(section_names):
                room = rooms[i]
                room_schedule = RoomSchedule.objects.create(curriculum=curriculum, room=room, section_name=section_name)
                room_schedules.append(room_schedule)

            class_schedule = ClassSchedule.objects.create(curriculum=curriculum)
            class_schedule.course_instructors.set(course_instructors)
            class_schedule.rooms.set(room_schedules)
            class_schedules.append(class_schedule)

        class_days_ids = request.POST.getlist('class_days')
        if not class_days_ids:
            messages.error(request, 'Please select at least one class day.')
            return redirect('generate_schedule')

        class_days = ClassSlots.objects.filter(pk__in=class_days_ids)

        generate_schedule = GenerateSchedule.objects.create()
        generate_schedule.class_schedules.set(class_schedules)
        generate_schedule.class_days.set(class_days)

        messages.success(request, 'Schedule generated successfully.')
        return redirect('generate_schedule')

    curriculums = Curriculum.objects.all()
    courses = Course.objects.all()
    instructors = Instructor.objects.all()
    rooms = Room.objects.all()
    class_slots = ClassSlot.objects.all()
    class_days = ClassSlots.objects.all()

    context = {
        'curriculums': curriculums,
        'courses': courses,
        'instructors': instructors,
        'rooms': rooms,
        'class_slots': class_slots,
        'class_days': class_days,
    }
    
    return render(request, 'generate_schedule.html', context)


# api views
from rest_framework import serializers, viewsets
# TODO: Make serializers for each model
