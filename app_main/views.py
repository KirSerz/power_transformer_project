from django.shortcuts import render
from .models import Substation
from .models import User
from .models import Transformer
from .models import DataDGA

from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, RedirectView
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

def post_list(request):
    
    return render(request, 'post_list.html', {})

class ApiAddDataDGA(View):
    def post(self, request, *args, **kwargs):
        context = {}
        context['status'] = 'ok'
        context['message'] = ''
        id_transformer = request.POST.get('unique_key')
        
        # TODO add model forms, validation form

        try:
            transformer = Transformer.objects.get(unique_key = unique_key)
        except:
            transformer = None

        if id_transformer:
            new_data_dga = transformer.upload_data(
                classification_score = None, 
                data_dga = request.POST.get('data_dga')
            )
        else:
            context['status'] = 'error'
            context['message'] = 'Invalid id transformer'
        
        return JsonResponse(context)

    def get(self, request, *args, **kwargs):
        context = {}
        context['status'] = 'error'
        context['message'] = 'Invalid id method'
        return JsonResponse(context)


