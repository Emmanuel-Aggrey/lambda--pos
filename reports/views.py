from django.shortcuts import render
from django.views.generic import FormView, DeleteView, ListView,DetailView
from accounts.models import CustomUser
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required()
# def users(request,business):
#     users = CustomUser.objects.select_related('business').filter(business_id=business)
#     print(users)
#     context = {
#         'users':users,
#     }
#     return render(request,'reports/employees.html', context) #JsonResponse(list(users),safe=False)


# class EmployeeListView(ListView):
#     template_name = 'reports/employees.html'
#     model = CustomUser
#     # paginate_by = 150
#     # is_paginated = True

#     def get_queryset(business):
#         query_set =  CustomUser.objects.select_related('business').filter(business_id=business).values()
#         return query_set