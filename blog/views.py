# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, CreateView, DetailView
from blog.blog_form import PostCreateForm
from blog.models import *


def blog_home(request):
    context = dict()
    request_context = RequestContext(request, context)
    return render_to_response('blog/index.html', request_context)


@login_required(login_url='login')
def create_post(request):
    context = dict()
    form = PostCreateForm(request.POST or None,
                          request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('blog_home'))
    context['form'] = form
    context['operation'] = 'Creación'
    context['subject'] = 'Post'
    request_context = RequestContext(request, context)
    return render_to_response('generic/generic_form.html',
                              request_context)


def imc_calculator(request):
    context = dict()
    request_context = RequestContext(request, context)
    return render_to_response('blog/imc_calculator.html',
                              request_context)


def ideal_weight_calculator(request):
    context = dict()
    request_context = RequestContext(request, context)
    return render_to_response('blog/ideal_weight_calculator.html',
                              request_context)


def basal_energy_waste(request):
    context = dict()
    request_context = RequestContext(request, context)
    return render_to_response('blog/energy_waste.html',
                              request_context)


class PostSingle(DetailView):
    template_name = 'blog/post_single.html'

    def get_object(self, queryset=None):
        post_pk = self.kwargs.get(self.pk_url_kwarg, None)
        if post_pk is not None:
            post = Post.objects.get(pk=post_pk)
        else:
            raise AttributeError("PK NOT FOUND")
        return post

    def get_context_data(self, **kwargs):
        context = super(PostSingle, self).get_context_data(**kwargs)
        return context
