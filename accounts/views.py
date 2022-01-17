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
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from accounts.forms import CustomUserChangeForm, CustomUserCreationForm

from .models import CustomUser
from django.views.generic.edit import UpdateView
from django.db import IntegrityError
from accounts.accounts_decorators import change_default_password


def employee(request, username):
    employee = get_object_or_404(CustomUser, username=username)

    data = {
        'id': employee.pk,
        'is_active': employee.is_active,
        'username': employee.username,
        'email': employee.email,
        'phone': employee.phone,
        'first_name': employee.first_name,
        'last_name': employee.last_name,
        'position': employee.position.name,
        'position_id': employee.position.pk,

    }
    return JsonResponse({'employee': data})


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            form.save(commit=False)
            business_name = request.user.business
            form.instance.business = business_name

            form.save()

            return JsonResponse({'success': 'user registration successful'})

        if form.errors:
            print(form.errors)
            return JsonResponse({'error': str(form.errors)})

    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def setDefaultPassword(defaultPassword):
    if defaultPassword  =='true':
        return True
    
 

@csrf_protect
# @csrf_exempt
def update_user(request, id):
    user = get_object_or_404(CustomUser, id=id)

    if request.method == 'POST':
        user_id = user
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        position = request.POST.get('position')
        phone = request.POST.get('phone')
        active = request.POST.get('active').capitalize()
        defaultPassword = request.POST.get('defaultPassword')
   

     
        try:
            user = user
            user.is_active = active
            user.username = username
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.phone = phone
            user.position_id = position
            password = setDefaultPassword(defaultPassword)
            if password is not None:
                user.set_password('changeme@123')

            user.save()
            
            return JsonResponse({'success': 'user update successful','isActive':str(user.is_active).lower()})
        except IntegrityError as ex:
            return JsonResponse({'error': f'update failed username is taken try again'})
      
       

        
def check_default_password(request):
    u = request.user.check_password("changeme@123")
    return JsonResponse({'default_password': u})


# @login_required()
def employees(request, business_slug):
    print("business_slug",business_slug)
    employees = CustomUser.objects.select_related(
        'business').filter(business__slug=business_slug).values('id', 'username', 'first_name', 'last_name', 'email', 'phone', 'position__name', 'is_active','is_staff')

    return JsonResponse({'data': list(employees)})

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
# @login_required
@csrf_exempt
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
    return JsonResponse({'message': state, "user_status": user_status})
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


def add_user_to_group(request, username):
    group = request.POST.get('group')
    # user = Group.objects.all()

    group = Group.objects.get(name=group)

    print(group)
    group.user_set.add(username)

    return JsonResponse({'username': username, 'group': f'{group}'})


def user_groups(request):
    groups = Group.objects.values('id', 'name')
    return JsonResponse({'groups': list(groups)})
