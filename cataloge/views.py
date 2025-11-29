from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def index(request):
    num_books=models.Book.objects.all().count()
    num_book_instanc=models.Bookinstance.objects.all().count
    num_book_avail=models.Bookinstance.objects.filter(status__exact='a').count()

    context={
        'num_books':num_books,
        'num_book_instanc':num_book_instanc,
        'num_book_avail':num_book_avail,
    }
    return render(request,'index.html',context)


class Bookgreate(LoginRequiredMixin,generic.CreateView):
    model=models.Book
    fields='__all__'
    success_url='/cataloge'
    template_name='create.html'

class register(generic.CreateView):
    form_class=UserCreationForm
    success_url='/accounts/login'
    template_name='registration/register.html'


class Bookdetail(LoginRequiredMixin,generic.DetailView):
    model=models.Book
    template_name='detail.html'
    context_object_name='books'