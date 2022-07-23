from django import forms 
from main.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widgets={'name':forms.TextInput(attrs={'class':"form-control"}),
        'rollno':forms.NumberInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'})
        }
