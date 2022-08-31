from django.shortcuts import render
from .forms import TableForm
from.models import Table
from django.views.generic import UpdateView, DetailView


class InputUpdateView(UpdateView):
    model = Table
    template_name = 'index/update.html'
    form_class = TableForm


def index(request):
    return render(request, 'index/main.html')

def input(request):
    error = ''
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма заполненна неккоректно'
    form = TableForm()
    data = {
        'form': form,
        "error": error
    }
    return render(request, 'index/input.html', data)
def table_page(request):
    articles = Table.objects.all()
    return render(request, 'index/table_page.html', {"articles": articles})