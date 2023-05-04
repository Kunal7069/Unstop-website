from django import forms
from .models import Section, Mentor, MentorContent

class SectionForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = ('name', 'mentor', 'mentor_content')

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ('user', 'headline', 'about')

class MentorContentForm(forms.ModelForm):
    class Meta:
        model = MentorContent
        fields = ('mentor', 'name', 'section', 'file')


