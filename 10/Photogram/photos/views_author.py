from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Author


class AuthorHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return '/author/'
        author = Author.get_me(self.request.user)
        return f'/author/{author.pk}'


class AuthorListView(ListView):
    template_name = 'author_list.html'
    model = Author
    context_object_name = 'authors'


class AuthorDetailView(DetailView):
    template_name = 'author_detail.html'
    model = Author
    context_object_name = 'author'

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     author = kwargs.get('author')
    #     kwargs.update(dict(dependent=author.dependents))
    #     return kwargs


# class AuthorCreateView(LoginRequiredMixin, CreateView):
#     template_name = "author_add.html"
#     model = Author
#     fields = '__all__'

#     def form_valid(self, form):
#         me = Author.get_me(self.request.user)
#         form.instance.user = me.user
#         return super().form_valid(form)


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "author_edit.html"
    model = Author
    fields = '__all__'


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'author_delete.html'
    success_url = reverse_lazy('author_list')