# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from personal_info.forms import PersonCreateForm, PersonUpdateForm
from personal_info.models import Person


class PersonList(ListView):
    model = Person
    template_name = 'personal_info/person_list.html'


class PersonCreate(CreateView):
    form_class = PersonCreateForm
    model = Person
    template_name = 'personal_info/person_create.html'
    success_url = reverse_lazy('personal_info:person_list')


class PersonDetail(DetailView):
    model = Person
    template_name = 'personal_info/person_detail.html'


class PersonUpdate(UpdateView):
    model = Person
    form_class = PersonUpdateForm
    template_name = 'personal_info/person_update.html'
    success_url = reverse_lazy('personal_info:person_list')


class PersonDelete(DeleteView):
    model = Person
    template_name = 'personal_info/person_delete.html'
    success_url = reverse_lazy('personal_info:person_list')
