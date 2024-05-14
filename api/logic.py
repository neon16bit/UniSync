from django.db import transaction
from .models import Curriculum, Instructor, Room, ClassSlot, ClassSchedule, CourseInstructor, RoomSchedule

@transaction.atomic
def generate_schedule():
    # Retrieve data
    curriculums = Curriculum.objects.all()
    instructors = Instructor.objects.all()
    rooms = Room.objects.all()
    class_slots = ClassSlot.objects.all()
    
    # Initialize empty list
    schedules = []
    
    for curriculum in curriculums:
        # Retrieve relevant courses and instructors
        for course in curriculum.courses.all():
            available_instructors = instructors.filter(is_guest=False)
            
            # Allocate rooms
            for room in rooms:
                # Determine the best available time slot
                for slot in class_slots:
                    schedule_entry = {
                        "curriculum": curriculum,
                        "course": course,
                        "room": room,
                        "slot": slot,
                        "instructors": available_instructors,
                    }
                    schedules.append(schedule_entry)

    for schedule_entry in schedules:
        # Create and save a `RoomSchedule` instance
        room_schedule = RoomSchedule(
            curriculum=schedule_entry["curriculum"],
            room=schedule_entry["room"],
        )
        room_schedule.save()
        
        # Create and save a `CourseInstructor` instance
        course_instructor = CourseInstructor(
            curriculum=schedule_entry["curriculum"],
            course=schedule_entry["course"]
        )
        course_instructor.save()
        course_instructor.instructors.set(schedule_entry["instructors"])
        
        # Create and save a `ClassSchedule` instance
        class_schedule = ClassSchedule(
            curriculum=schedule_entry["curriculum"],
        )
        class_schedule.save()
        class_schedule.course_instructors.add(course_instructor)
        class_schedule.rooms.add(room_schedule)
