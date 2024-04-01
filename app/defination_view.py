import json

from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection

from app.serializers import DefinitionSerializer


@api_view(['POST'])
def insert_definition(request):
    name = request.data.get('name')
    detail = request.data.get('detail')
    deftarget = request.data.get('deftarget')

    try:
        data = {
            "name": name,
            "detail": detail,
            "deftarget": deftarget
        }

        serializer = DefinitionSerializer(data=data)
        if serializer.is_valid():

            with connection.cursor() as cursor:
                cursor.execute("CALL insert_definition(%s, %s, %s, %s)", [
                    name, detail, json.dumps(deftarget), None])

                inserted_id = cursor.fetchone()[0]
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"id": inserted_id, "message": "Locker inserted successfully."}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def update_definition(request, id):
    name = request.data.get('name')
    detail = request.data.get('detail')
    deftarget = request.data.get('deftarget')

    try:
        data = {
            "name": name,
            "detail": detail,
            "deftarget": deftarget
        }

        serializer = DefinitionSerializer(data=data)
        if serializer.is_valid():
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT EXISTS(SELECT * FROM tbl_defination WHERE id = %s)", [id])
                locker_exists = cursor.fetchone()[0]

                if not locker_exists:
                    return Response({"error": "Definition does not exist."}, status=status.HTTP_404_NOT_FOUND)

                cursor.execute("CALL update_definition(%s, %s, %s, %s)",
                               [id, name, detail, json.dumps(deftarget)])
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"id": id, "message": "Definition updated successfully."}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
