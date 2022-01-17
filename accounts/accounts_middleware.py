from django.shortcuts import redirect,reverse,HttpResponseRedirect
from django.conf import settings
from django.contrib import auth
from datetime import datetime, timedelta

def check_default_password_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        default_password = request.user.check_password('aggrey123')

        

        # if default_password:
        #     return redirect('change_password')
        return redirect('change_password') if default_password else redirect('home')

        response = get_response(request)
        # return HttpResponseRedirect(reverse('change_password')) if default_password else HttpResponseRedirect(reverse('home'))

        # Code to be executed for each request/response after
        # the view is called.

        


        return response

    return middleware



class AutoLogout:
  def process_request(self, request):
    if not request.user.is_authenticated() :
      #Can't log out if not logged in
      return

    try:
      if datetime.now() - request.session['last_touch'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
        auth.logout(request)
        del request.session['last_touch']
        return
    except KeyError:
      pass

    request.session['last_touch'] = datetime.now()