

from django.forms import ModelForm
from .models import Project


# this class is gonna generate a form based on the field of Project. so fields is a default var
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'
        fields=['title','featured_iamge', 'description', 'demo_link', 'source_link', 'tags']