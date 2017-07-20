# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from .models import Post
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView
from django.views.generic.detail import DetailView

class Index(TemplateView):
	template_name = 'index.html'


class PostView(CreateView):
	model = Post
	template_name = 'post.html'
	fields = ['name', 'title', 'sub_title']
	success_url = '/'

class PostListView(ListView):
	"""docstring for PostListView"""
	template_name = 'list.html'
	model = Post
	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		context['post'] = Post.objects.all()
		return context

class PostDetailView(DetailView):

	model = Post
	template_name = 'post_detail.html'
	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		context['post'] = Post.objects.all()
		return context