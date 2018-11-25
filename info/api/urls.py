from django.conf.urls import url
from django.views.generic import TemplateView

info_url = [
    url('', TemplateView.as_view(template_name='index.html'), name='index'),
]
