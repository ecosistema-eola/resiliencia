from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProjectProposal, Indicator, Profile
from .models import Risk
from .models import ResilienceIndicator
from .models import Project



# Formulario para actualizar valor del indicador
class IndicatorForm(forms.ModelForm):
    class Meta:
        model = Indicator
        fields = ['value']


# Formulario para crear propuestas de proyecto
class ProposalForm(forms.ModelForm):
    class Meta:
        model = ProjectProposal
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


# Formulario de registro personalizado
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'role', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user.profile.role = self.cleaned_data['role']
            user.profile.save()
        return user

#Riesgos

class RiskForm(forms.ModelForm):
    class Meta:
        model = Risk
        fields = ['name', 'residual', 'financial_impact', 'csv_file', 'gpt_link', 'is_territory']

#subir indicadores

class ResilienceIndicatorForm(forms.ModelForm):
    class Meta:
        model = ResilienceIndicator
        fields = ['name', 'description', 'unit', 'baseline', 'target', 'year_target', 'risk_focus']

#proyectos 


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'indicator', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
