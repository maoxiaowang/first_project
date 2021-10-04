from django import forms

from personal_info.models import Person


class PersonCreateForm(forms.ModelForm):

    class Meta:

        model = Person
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'id': 'name_id', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'id': 'age_id', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'id': 'gender_id', 'class': 'form-select'}),
            'id_card': forms.TextInput(attrs={'id': 'id_card_id', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'id': 'address_id', 'class': 'form-control'}),
            'temperature': forms.NumberInput(attrs={'id': 'temperature_id', 'class': 'form-control', 'step': '0.1'}),
        }

        labels = {
            'name': '名字',
        }


class PersonUpdateForm(PersonCreateForm):
    pass
