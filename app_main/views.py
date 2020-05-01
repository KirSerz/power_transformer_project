from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, RedirectView
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

class BasePage(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context['status'] = 'ok'
        return JsonResponse(context)