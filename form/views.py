from django.shortcuts import render
from django.views.generic import CreateView, ListView
from form.models import Form
from form.forms import UserModelForm


class CreateUser(CreateView):
    model = Form
    form_class = UserModelForm
    template_name = 'user.html'
    success_url = '/list/'
    

class ListUser(ListView):
    model = Form
    template_name = 'list.html'
    context_object_name = 'Form'
