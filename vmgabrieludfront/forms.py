"""Forms of Vmgabrieludfront APP"""

# Libraries
from django import forms

# Models
from . import models

class PeriphepaltypeForm(forms.ModelForm):
    """Form to Periphepaltype"""

    class Meta:
        model = models.periphepaltype.Periphepaltype
        fields = ["name", "description", ]


class PeriphepalForm(forms.ModelForm):
    """Form to Periphepal"""
    type_periphepal = forms.ModelChoiceField(queryset=models.periphepaltype.Periphepaltype.objects.all())

    class Meta:
        model = models.periphepal.Periphepal
        fields = ["name", "description", "type_periphepal", ]


class CameraForm(forms.ModelForm):
    """Form to Camera"""

    class Meta:
        model = models.camera.Camera
        fields = ["name", ]


class CameraperiphepalForm(forms.ModelForm):
    """Form to Cameraperiphepal"""
    camera = forms.ModelChoiceField(queryset=models.camera.Camera.objects.all())
    periphepal = forms.ModelChoiceField(queryset=models.periphepal.Periphepal.objects.all())

    class Meta:
        model = models.cameraperiphepal.Cameraperiphepal
        fields = ["camera", "periphepal", ]


