from decouple import config
def business_name(request):
    return {'business_name':config('BUSINESS_NAME'),'business':config('BUSINESS_CONTACT')}

def business_contact(request):
    return {'business_contact':config('BUSINESS_CONTACT')}
