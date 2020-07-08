from django import forms
from .models import Contact
import datetime
#from notes.models import Note


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
        ]

#class NoteForm(forms.ModelForm):
#     class Meta:
#         model = Note
#         fields = [
#             'note'
#         ]

        widgets = {
        'birthday': forms.DateInput(format=('%m/%d/%Y'), attrs=
        {'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }

class DateForm(forms.Form):
    day = forms.DateField(initial=datetime.date.today)
print(DateForm())