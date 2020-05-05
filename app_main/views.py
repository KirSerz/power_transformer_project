from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import (CreateView, DetailView, ListView,
                                  RedirectView, TemplateView)

from .models import DataDGA, Substation, Transformer, User


def post_list(request):
    id_substation=1
    context={}
    try:
        substation=Substation.objects.get(id=id_substation)
        context["substation"]=substation
        transformers=Transformer.objects.filter(substation=substation.id)
        transformer_data = {item.id: {
            "transformer":item,
            'data':list()
        } for item in transformers}
    except:
        transformers=[]
        transformer_data={}
    
    data_DGA = DataDGA.objects.filter(transformer__in = transformers).order_by('date')
    for dga in data_DGA:
        transformer_data[dga.transformer.id]["data"].append(dga)

    context["data_transformers"]=list(transformer_data.values())
    return render(request, 'post_list.html', context)


class ApiAddDataDGA(View):
    def post(self, request, *args, **kwargs):
        context = {}
        context['status'] = 'ok'
        context['message'] = ''
        unique_key = request.POST.get('unique_key')
        
        # TODO add model forms, validation form

        try:
            transformer = Transformer.objects.get(unique_key = unique_key)
        except:
            transformer = None
        
        # TODO classifications data dga and calculation classification_score
        
        if transformer:
            transformer.upload_data(
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

