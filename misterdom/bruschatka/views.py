from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

menu = [{'title': "Кровля", 'url_name': 'krovlya'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "войти", 'url_name': 'login'},

        ]


class BruschatkaHome(ListView):
    model = Bruschatka
    template_name = 'bruschatka/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context


# def index(request):
#     posts = Bruschatka.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'bruschatka/index.html', context=context)

def about(request):
    return render(request, 'bruschatka/about.html', {'menu': menu, 'title': 'О сайте'})


class Krovlya(CreateView):
    form_class = AddPostForm
    template_name = 'bruschatka/krovlya.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление товара'
        context['menu'] = menu
        return context
# def krovlya(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'bruschatka/krovlya.html', {'form': form, 'menu': menu, 'title': 'Кровля'})

def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def show_post(request, post_slug):
#     post = get_object_or_404(Bruschatka, slug=post_slug)
#
#     context = {
#         'posts': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'bruschatka/post.html', context=context)


class ShowPost(DetailView):
    model = Bruschatka
    template_name = 'bruschatka/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


class BruschatkaCategory(ListView):
    model = Bruschatka
    template_name = 'bruschatka/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Bruschatka.object.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вид - ' + str(context['post'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

# def show_category(request, cat_id):
#     posts = Bruschatka.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по категориям',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'bruschatka/index.html', context=context)
