from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Player, HighSchoolPlayer, ProPlayer
from .serializers import *

@api_view(['GET'])
def players_list(request):
    data = Player.objects.all()

    serializer = PlayerSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def players_detail(request, utr_id):
    try:
        student = Player.objects.get(utr_id=utr_id)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PlayerSerializer(student, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)