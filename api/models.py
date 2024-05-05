from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=3, unique=True, primary_key=True,)
    room_capacity = models.IntegerField()
    
    def __str__(self):
        return f'{self.room_number} - Capacity: {self.room_capacity}'
 
    
class Course(models.Model):
    course_code = models.CharField(max_length=12, unique=True, primary_key=True,)
    course_title = models.CharField(max_length=100)
    course_credit = models.DecimalField(max_digits=3, decimal_places=2)
    course_timeperweek = models.DecimalField(max_digits=3, decimal_places=2)
    course_content = models.TextField()
    
    
class Curriculum(models.Model):
    SEMESTERS = [
        ('1.1', '1st Year 1st Semester'),
        ('1.2', '1st Year 2nd Semester'),
        ('2.1', '2nd Year 1st Semester'),
        ('2.2', '2nd Year 2nd Semester'),
        ('3.1', '3rd Year 1st Semester'),
        ('3.2', '3rd Year 2nd Semester'),
        ('4.1', '4th Year 1st Semester'),
        ('4.2', '4th Year 2nd Semester'),
    ]
    
    curriculum_semester = models.CharField(max_length=3, unique=True, primary_key=True, choices=SEMESTERS)
    courses = models.ManyToManyField(Course,)
    
    def get_course_list(self):
        return self.courses.values_list('course_code', flat=True)
    
    def __str__(self):
        course_list = ', '.join(self.get_course_list())
        return f'{self.curriculum_semester} - Courses: {course_list}'

    

class ClassSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return f'{self.start_time} - {self.end_time}'

class ClassSlots(models.Model):
    DAYS = [
        ('SUN', 'Sunday'),
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
    ]
    
    day = models.CharField(max_length=3, choices=DAYS, unique=True, primary_key=True,)
    class_slots = models.ManyToManyField(ClassSlot,)
    
    def __str__(self):
        slots = ', '.join([str(slot) for slot in self.class_slots.all()])
        return f'{self.day} - {slots}'
    
class Instructor(models.Model):
    DESIGNATIONS = [
        ('L', 'Lecturer'),
        ('SL', 'Senior Lecturer'),
        ('P', 'Professor'),
        ('AP', 'Adjunct Professor'),
        ('AS', 'Assistant Professor'),
        ('DH', 'Departmental Head'),
        ('AD', 'Adjunct'),
    ]
    
    DEPARTMENT = [
        ('CSE', 'Computer Science and Engineering'),
        ('EEE', 'Electrical and Electronic Engineering'),
        ('CE', 'Civil Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
    ]
        
    email = models.EmailField(unique=True, primary_key=True,)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14, unique=True,)
    designation = models.CharField(max_length=2, choices=DESIGNATIONS)
    department = models.CharField(max_length=3, choices=DEPARTMENT)
    preferred_time = models.ForeignKey(ClassSlot, on_delete=models.PROTECT)
    #max_class_per_day = models.IntegerField(null=True, blank=True)
    
class RoomSchedule(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=1)
    
    class Meta:
        unique_together = ('curriculum', 'room', 'section_name',)
        
    def __str__(self):
        return f'{self.curriculum.curriculum_semester} - {self.section_name} - {self.room}'

class CourseInstructor(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructors = models.ManyToManyField(Instructor)
        
     
class ClassSchedule(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    course_instructors = models.ManyToManyField(CourseInstructor)
    rooms = models.ManyToManyField(RoomSchedule)
    max_class_per_week = 4
    
class GenetareSchedule(models.Model):
    class_schedule = models.ManyToManyField(ClassSchedule)
    class_days = models.ManyToManyField(ClassSlots)