from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', BruschatkaHome.as_view(), name='home'),
    path('krovlya/', krovlya, name='krovlya'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', BruschatkaCategory.as_view(), name='category'),
]
