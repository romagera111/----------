from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

# Create your views here.
def news_home(request):
    news = Articles.objects.all()
    #Если я хочу как-то отсортировать или вывести определённое кол-во, то использую order_by
    news = Articles.objects.order_by('date')
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        else:
            error='Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)