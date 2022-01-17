import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect

from accounts.forms import CustomUserChangeForm, CustomUserCreationForm

# from django.db.models.auth import Group
from .models import CustomUser


@login_required
def index(request):
    print("request",request)
    return render(request, 'index.html')


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

          
           
            form.save()

            return redirect('/')

        if form.errors:
            print(form)
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def check_default_password(request):
    u = request.user.check_password("changeme@123")
    return JsonResponse({'default_password': u})


# @login_required()
def employeess(request, business_slug):
    employees = CustomUser.objects.select_related(
        'business').filter(business__slug=business_slug).values()
    
  
    return JsonResponse({'data':list(employees)})

    # return render(request, 'accounts/employees.html', {'users': users})


# class EmployeeListView(ListView):
#     template_name = 'accounts/employees.html'
#     model = CustomUser
#     # paginate_by = 150
#     # is_paginated = True

#     def get_queryset(business):
#         query_set =  CustomUser.objects.select_related('business').filter(business_id=business).values()
#         return query_set


@permission_required('delete_customuser.Can delete user', raise_exception=True)
@login_required
def delete_user(request, id):
    user = CustomUser.objects.get(id=id)

    user.delete()
    messages.success(
        request, f'{user.first_name} {user.last_name} is deleted successfully!')
    return redirect('/users')


@permission_required('delete_customuser.Can delete user', raise_exception=True)
@login_required
def deactivate_activate_user(request, id):
    user = CustomUser.objects.get(id=id)
    if user.is_active:
        user.is_active = False
        user.save()
        # messages.success(
        #     request, f'{user.first_name} {user.last_name} is made inactive !')
    elif not user.is_active:
        user.is_active = True
        user.save()
        # messages.success(
        #     request, f'{user.first_name} {user.last_name} is made active !')

    # print()
    # is_nice = True
    state = f"{user.get_full_name} Account Activated" if user.is_active else f"{user.get_full_name} Account Deactivated"
    user_status = user.is_active
    # print("state",state)
    return JsonResponse({'message': state,"user_status":user_status})
    # return redirect(user.get_users_by_business_name)


@login_required
def resetPassword(request, user):
    user = CustomUser.objects.get(id=user)
    user.set_password(request.POST.get('changeme@123', 'changeme@123'))
    user.save()
    context = {'user': user.get_full_name,
               'message': 'Password changed and set to default (changeme@123)'
               }
    return JsonResponse(context)


def add_user_to_group(request,username):
    group = request.POST.get('group')
    # user = Group.objects.all()

    group = Group.objects.get(name=group) 

    print(group)
    group.user_set.add(username)


    return JsonResponse({'username':username,'group':f'{group}'})



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)