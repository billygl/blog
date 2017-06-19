from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def main(request):
    template = loader.get_template('main.html')
    context = {}
    return HttpResponse(template.render(context, request))

def detalle(request, post_id):
    print(post_id)
    template = loader.get_template('detalle.html')
    context = {
        'post_id' : post_id
    }
    return HttpResponse(template.render(context, request))
