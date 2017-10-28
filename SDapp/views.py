# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from SDapp.models import Customer,Region,Nation,Orders,Part,Supplier,Partsupp,Lineitem
import operator
from django.db.models import Q
from django.shortcuts import render_to_response

# Create your views here.
def list_users(request):
	users = Customer.objects.all()
	result = search(request)
	return render(request,template_name ='list_users.html',context={'users':result})


def search(request):
    query = request.GET.get('q')
    if query:
        query_list = query.split()
        qset = (
            reduce(operator.and_,(Q(c_name__icontains=q) for q in query_list)) |
            reduce(operator.and_,(Q(c_address__icontains=q) for q in query_list)) |
            reduce(operator.and_,(Q(c_comment__icontains=q) for q in query_list))
        )
        results = Customer.objects.filter(qset)
    else:
        results = []
    print results
    print "sadfffffsadsadf"
    return results