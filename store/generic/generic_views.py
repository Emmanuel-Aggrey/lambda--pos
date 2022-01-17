from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from store.models import Generic as Generic_Category
from store.serializers import GenericSerializer


@api_view(['GET', 'POST'])
def generic_views(request):
    """
    LIST ALL GENERICS, OR CREATE A NEW GENERIC
    """

    if request.method == 'GET':

        generic = Generic_Category.objects.all()

        serializer = GenericSerializer(generic, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GenericSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE','POST'])
def generic_view(request, pk):
    """
    UPDATE, GET OR DELETE A GENERIC
    """
    try:
        generic = Generic_Category.objects.get(pk=pk)
    except Generic_Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = GenericSerializer(generic)
        return Response(serializer.data)

    elif request.method == 'PUT' or 'POST':
        serializer = GenericSerializer(generic, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = GenericSerializer(generic,
                                       data=request.data,
                                       partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        generic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
