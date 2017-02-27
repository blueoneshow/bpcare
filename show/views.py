# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response


def show(request):
        choirs = ['pccb', 'vienna', 'libera', 'voxangeli']
        return render_to_response('show.html', {'choirs':choirs})
  
def pccb(request):
        words = [ 'a', 'b', 'c']
        return render_to_response('pccb.html', {'words':words})
 