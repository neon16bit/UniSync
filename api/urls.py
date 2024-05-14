from django.urls import path
from .import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('curriculums/', views.curriculum_list, name='curriculum_list'),
    path('rooms/', views.room_list, name='room_list'),
    path('faculty_members/', views.faculty_member_list, name='faculty_member_list'),
    path('generate_schedule/', views.generate_schedule, name='generate_schedule'),
    path('curriculum_fields/', views.curriculum_fields, name='curriculum_fields')
]
