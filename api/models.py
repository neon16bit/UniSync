from django.db import models

class Room(models.Model):
    room_number = models.IntegerField(max_length=10, unique=True, primary_key=True,)
    room_capacity = models.IntegerField()

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
    curriculum_courses = models.ForeignKey(Course, on_delete=models.PROTECT)
           
class faculty_member(models.Model):
    DESIGNATIONS = [
        ('L', 'Lecturer'),
        ('SL', 'Senior Lecturer'),
        ('P', 'Professor'),
        ('AP', 'Assistant Professor'),
        ('DH', 'Departmental Head'),
        ('AD', 'Adjoint'),
    ]
    
    DEPARTMENT = [
        ('CSE', 'Computer Science and Engineering'),
        ('EEE', 'Electrical and Electronic Engineering'),
        ('CE', 'Civil Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
    ]
        
    email = models.EmailField(unique=True, primary_key=True,)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=11,)
    designation = models.CharField(max_length=2, choices=DESIGNATIONS)
    department = models.CharField(max_length=100)
    