from django.shortcuts import render, redirect, HttpResponse
from .models import Articles
from .forms import AddNews, CommentForm
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'dateNews/new.html', {'news': news} )

class NewsDetailView(DetailView, FormMixin):
    model = Articles
    template_name = 'dateNews/details_view.html'
    context_object_name = 'article'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('news-detail', kwargs={'pk':self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return  self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.save()
        return super().form_valid(form)


def create(request):
    error =''
    if request.method == 'POST':
        form = AddNews(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('news_home')
        else:
            error = "Неправильно заполнено"

    form = AddNews()
    date = {
        'form': form,
        'error': error
    }

    return render(request, 'dateNews/create.html', date)
