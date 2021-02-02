from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import nltk
import re
from nltk.corpus import stopwords
from .models import Scrapping
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
def freq(request):

    context = {}
    content={}
    word=''
    
    if request.method == 'POST':
        URL = request.POST.get('url')
        obj = Scrapping.objects.filter(Site_URL=URL).first()

            

        if obj:
            context['Site_URL']=URL
            context['Top_word']=obj.Top_word
            print(context)
        else:
            content = scrap(URL)
            for x in list(content)[0:10]:
                word+=x+':'+str(content[x])+' ; '
                
            Scrapping.objects.create(Site_URL=URL, Top_word= word)
            context['Site_URL']=URL
            context['Top_word']=word
            print(context)
        obj1 = Scrapping.objects.get(Site_URL=URL)
        x = str(obj1.id)
        return redirect('../result/'+x+'/')
            
    return render(request, 'form.html', context)

def scrap(lk):
    url=lk
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent,'html.parser')
    para = soup.get_text()
    para = re.sub('[^a-zA-Z]',' ',para)
    




    x=word_count(para)
    return x
 

def word_count(str1):

    counts = dict()
    top={}

    words = str1.split()
    t1= [word for word in words if not word in ENGLISH_STOP_WORDS]
    
    for word in t1:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    del counts['s']

    sorted_dict = {}
    sorted_keys = sorted(counts, key=counts.get)  # [1, 3, 2]

    for w in sorted_keys:
        sorted_dict[w] = counts[w]
    

    for x in list(reversed(list(sorted_dict)))[0:10]:
        
        top[x]=sorted_dict[x]
    
    
    return top



def res(request,pk_test):
    pk_test=int(pk_test)
    context={}
    profile=Scrapping.objects.get(id=pk_test)
    context={'profile':profile}
    print(context)
    return render(request, 'result.html',context)
