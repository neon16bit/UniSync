# Generated by Django 5.0.2 on 2024-05-11 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_instructor_is_depertmental_head_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curriculum',
            options={'ordering': ['curriculum_semester', 'is_diploma_curriculum']},
        ),
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ['department', 'designation', 'name']},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['room_number']},
        ),
    ]
