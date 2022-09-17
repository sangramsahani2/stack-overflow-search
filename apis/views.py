import requests
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import qustions
import json

qname = ''
def index(request):
   
    return render(request,'index.html')

    

    
@csrf_exempt
def getdata(request):
    
    qname = request.POST['qname']
    data = qustions.objects.filter(title__contains= qname)
    if not data:
        urls = 'https://api.stackexchange.com/2.3/search/advanced?&order=desc&sort=activity&accepted=True&tagged='+qname+'&site=stackoverflow'
        data = requests.get(urls).json()
        # data1 = json.loads(data) # first convert to a dict
        item = data['items']
        for i in item:
            s = qustions( tag = i['tags'] , link = i['link'] , title = i['title'] )
            s.save()
        print('saved')

            
    
        
    paginator = Paginator(data, 10)
    page_num = request.GET.get('page') or 1
    page = paginator.get_page(page_num)
    
    context = {
        'count' : paginator.count,
        'page' : page
    }
       

    return (render(request,'result.html',context))


    
