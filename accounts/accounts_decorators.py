from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth import REDIRECT_FIELD_NAME

# def not_in_site(user):
#     try:
#         if user.belongs_to_site:
#             return True       #Condition's will come here
#         return False
#     except:
#         pass
   

# class SiteRequiredMixin(object):
#     """"Custom user passes test Required Mixin"""
#     @method_decorator(user_passes_test(not_in_site, login_url='/warehouse_registrations/'))
#     def dispatch(self, request, *args, **kwargs):
#         return super(SiteRequiredMixin, self).dispatch(request, *args, **kwargs)




def change_default_password(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='change_password'):
    '''
    Decorator for views that checks that the logged in user is using the default password,
    redirects to the change_password page if True.
    '''

    
      
  
    actual_decorator = user_passes_test(

    lambda  user: not user.check_password('changeme@123'),
    
    login_url=login_url,
    redirect_field_name=redirect_field_name
        
    )
    
    if function:
        # print(login_url,redirect_field_name)
        return actual_decorator(function)
    return actual_decorator

    
    
   
# FUCNTION DECORATOS

def construction_manager_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user belongs to site,
    redirects to the log-in page if necessary.
    '''
    
    actual_decorator = user_passes_test(
    # lambda u: u.is_active and u.is_student or u.is_superuser,  
    lambda user: user.is_construction_manager or user.is_superuser or user.is_staff or user.is_project_manager,
    login_url=login_url,
    redirect_field_name=redirect_field_name
    )
    
    if function:
        return actual_decorator(function)
    return actual_decorator


def project_manager_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user belongs to site,
    redirects to the log-in page if necessary.
    '''
    
    actual_decorator = user_passes_test(
    # lambda u: u.is_active and u.is_student or u.is_superuser,  
    lambda user: user.is_project_manager or user.is_superuser or  user.is_staff,
    login_url=login_url,
    redirect_field_name=redirect_field_name
    )
        
    if function:
        return actual_decorator(function)
    return actual_decorator


def warehouse_manager(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user belongs to site,
    redirects to the log-in page if necessary.
    '''
    
    actual_decorator = user_passes_test(
    # lambda u: u.is_active and u.is_student or u.is_superuser,  
    lambda user: user.is_warehouse_manager or user.is_superuser or  user.is_staff,
    login_url=login_url,
    redirect_field_name=redirect_field_name
    )
        
    if function:
        return actual_decorator(function)
    return actual_decorator




def all_heads_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user belongs to site,
    redirects to the log-in page if necessary.
    '''
    
    actual_decorator = user_passes_test(
    # lambda u: u.is_active and u.is_student or u.is_superuser,  
    lambda user:  user.is_superuser or user.is_staff,
    login_url=login_url,
    redirect_field_name=redirect_field_name
    )
        