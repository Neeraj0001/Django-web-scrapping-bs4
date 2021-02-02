from django.shortcuts import render, redirect
from django.http import HttpResponse


def freq(request):
    context = {}
    if request.method == 'POST':
        URL = request.POST.get('url')
        print(URL)
    return render(request, 'form.html', context)
