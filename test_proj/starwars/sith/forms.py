from django import forms

from starwars.sith.models import Recruter, Answer


class RecruterForm(forms.ModelForm):

    class Meta:
        model = Recruter
        exclude = ('is_shadow_hand', 'sith')


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = '__all__'
        widgets = {
            'recruter': forms.HiddenInput()
        }
