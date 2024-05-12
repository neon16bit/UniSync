import datetime
from django import forms
from api.models import ClassSlot
from django.core.exceptions import ValidationError
import re

# class AMPMTimeField(forms.TimeField):
#     def to_python(self, value):
#         if value is None:
#             return None

#         # Check if the input value matches the expected format hh:mm AM/PM
#         pattern = r'^(0?[1-9]|1[0-2]):([0-5]\d)\s?(AM|PM)$'
#         match = re.match(pattern, value.upper())

#         if not match:
#             raise ValidationError('Invalid time format. Please use hh:mm AM/PM.')

#         hour = int(match.group(1))
#         minute = int(match.group(2))
#         meridiem = match.group(3)

#         # Convert to 24-hour format
#         if meridiem == 'PM' and hour < 12:
#             hour += 12
#         elif meridiem == 'AM' and hour == 12:
#             hour = 0

#         return datetime.time(hour, minute)


class ClassSlotForm(forms.ModelForm):
    
    start_time = forms.TimeField(
        input_formats=['%I:%M %p'],
        widget=forms.TimeInput(format='%I:%M %p')
    )
    end_time = forms.TimeField(
        input_formats=['%I:%M %p'],
        widget=forms.TimeInput(format='%I:%M %p')
    )
    
    class Meta:
        model = ClassSlot
        fields = ['start_time', 'end_time']
    
    
