from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import TemplateView


class TestIndex(TemplateView):
    template_name = 'first_app/index.html'

    def get_context_data(self, **kwargs):
        return {'word': 'hello world'}
