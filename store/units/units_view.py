from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.
from store.models import Unit


@api_view(['GET', 'POST', 'PUT'])
# @csrf_exempt
def units(request, id=None):
    units = Unit.objects.values()

    if request.method == 'GET' and id is None:

        # return JsonResponse({'data': list(units)})

        return Response({'data': units}, status=status.HTTP_200_OK)

    elif request.method == 'GET' and id is not None:

        units = units.get(id=id)

        data = {
            'unit_full_name': units.get('name'),
            'name': units.get('unit'),
            'id': units.get('id'),
            'available': units.get('available')
        }

        return Response(data, status=status.HTTP_200_OK)

    if request.method == 'POST'  and id is None:
        unit_full_name = request.POST.get('name').upper()
        unit_name = request.POST.get('unit').upper()
        available = request.POST.get('available').capitalize()

        units = units.create(name=unit_full_name,unit=unit_name, available=available)


        #return JsonResponse({'message':f'{unit_name} added to unit'})
        return Response({'message': 'Unit created successfully'}, status=status.HTTP_201_CREATED)


    elif  request.method == 'POST' and id is not None:
        # print('put request running',units)


        unit = Unit.objects.get(id=id)
        unit_full_name = request.POST.get('name').upper()
        unit_name = request.POST.get('unit').upper()
        available = request.POST.get('available').capitalize()


        unit = unit
        unit.name = unit_full_name
        unit.available = available
        unit.unit = unit_name
        


        unit.save(update_fields=['name','available','unit','date_updated'])

        #return JsonResponse({'message':'unit updated successfully'})
        return Response({'message': 'unit updated successfully'}, status=status.HTTP_200_OK)
    else: 
        return Response({'message':'unit not found'}, status=status.HTTP_203_BAD_REQUEST)
