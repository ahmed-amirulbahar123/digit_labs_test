import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection

from app.serializers import LockerSerializer


@api_view(['POST'])
def insert_locker(request):
    name = request.data.get('name')
    description = request.data.get('description')
    lockerdata = request.data.get('lockerdata')

    try:
        data = {
            "name": name,
            "description": description,
            "lockerdata": lockerdata
        }

        serializer = LockerSerializer(data=data)
        if serializer.is_valid():

            with connection.cursor() as cursor:
                cursor.execute("CALL insert_locker(%s, %s, %s, %s)", [
                    name, description, json.dumps(lockerdata), None])

                inserted_id = cursor.fetchone()[0]
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"id": inserted_id, "message": "Locker inserted successfully."}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def update_locker(request, id):
    name = request.data.get('name')
    description = request.data.get('description')
    lockerdata = request.data.get('lockerdata')

    try:
        data = {
            "name": name,
            "description": description,
            "lockerdata": lockerdata
        }

        serializer = LockerSerializer(data=data)
        if serializer.is_valid():
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT EXISTS(SELECT * FROM tbl_locker WHERE id = %s)", [id])
                locker_exists = cursor.fetchone()[0]

                if not locker_exists:
                    return Response({"error": "Locker does not exist."}, status=status.HTTP_404_NOT_FOUND)

                cursor.execute("CALL update_locker(%s, %s, %s, %s)",
                               [id, name, description, json.dumps(lockerdata)])
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"id": id, "message": "Locker updated successfully."}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
