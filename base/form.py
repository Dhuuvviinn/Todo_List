from django.forms import ModelForm
from .models import TODO
class todoForm(ModelForm):
    class Meta:
        model = TODO
        fields = ["title","status","priority"]