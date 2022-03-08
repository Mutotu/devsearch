
from tkinter import Widget
from django.forms import ModelForm
from django import forms
from .models import Project


# this class is gonna generate a form based on the field of Project. so fields is a default var
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'
        fields=['title','featured_iamge', 'description', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__( *args, **kwargs)
        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder':'Add title'})
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            