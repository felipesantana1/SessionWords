# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def index(request):
    return render(request, 'session_words/index.html')

def showWords(request):

    if 'font' in request.POST:
        font = '200%'
    else:
        font = '100%'

    if 'word' not in request.session:

        request.session['word'] = []

    words = request.session['word']
    words.append({

        'newWord': request.POST['words'],
        'color': request.POST['colors'],
        'font': font,
        'time': strftime("%b-%d-%Y %H:%M %p", localtime())
    })

    request.session['word'] = words

    return redirect('/')

def clearSess(request):
    request.session.clear()
    return redirect('/')