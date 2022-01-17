

def default_password_check(request):
    try:
        u = request.user.check_password("changeme@123")

        return {'default_password_check':u}
    except:
        pass
    