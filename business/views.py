from django.shortcuts import render
from .models import Supplier
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.db import IntegrityError
# Create your views here.


def suppliers(request):
    suppliers = Supplier.objects.values().filter(available=True)

    return JsonResponse({'data': list(suppliers)})


def create_supplier(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        location = request.POST.get('location')
        available = request.POST.get('available').capitalize()
        description = request.POST.get('description')

        try:
            supplier = Supplier.objects.create(name=name, phone=phone,email=email,location=location,
                                available=available, description=description)
            return JsonResponse({'message': 'supplier created successfully'})
        except IntegrityError as ex:
            print(ex.args)
            return JsonResponse({'error':'supplier with this name already exist'})
        
# def get_supplier(request, id):{

# }


def update_supplier(request, id):
    supplier = Supplier.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        location = request.POST.get('location')
        available = request.POST.get('available').capitalize()
        description = request.POST.get('description')

        supplier = supplier
        supplier.name = name
        supplier.email = email
        supplier.phone = phone
        supplier.location = location
        supplier.description = description
        supplier.available = available

        supplier.save()

        return JsonResponse({'message': 'supplier updated successfully', 'supplier_name': name})

    if request.method == 'GET':

        suplier = {
            'id': supplier.id,
            'name': supplier.name,
            'email': supplier.email,
            'phone': supplier.phone,
            'location': supplier.location,
            'available': supplier.available,
            'description': supplier.description,
        }

        return JsonResponse({'supplier': suplier})
