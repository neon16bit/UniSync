from django.shortcuts import render
from .models import Course, Curriculum, Room, Instructor

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



# api views
from rest_framework import serializers, viewsets
# TODO: Make serializers for each model
