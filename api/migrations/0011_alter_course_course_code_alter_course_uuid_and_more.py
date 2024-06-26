# Generated by Django 5.0.2 on 2024-05-12 15:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20240512_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='classslot',
            unique_together={('start_time', 'end_time')},
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('course_code', 'is_diploma_course')},
        ),
    ]
