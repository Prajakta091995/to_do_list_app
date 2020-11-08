from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from to_do_logic.serializers import ToDoListSerializer
from to_do_logic.models import to_do_list

class ToDoListAPIView(APIView):

    #show to do list
    def get(self, request):
        print('Executing APIView get list...')
        todo = to_do_list.objects.all()
        serializer = ToDoListSerializer(todo, many=True)
        return Response(serializer.data)

    #create to do list
    def post(self, request):
        print('Executing APIView post ...')
        serializer = ToDoListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


class ToDoDetailAPIView(APIView):

    #show specific to do
    def get(self, request, pk):
        print("Executing APIView get object...")
        todo = to_do_list.objects.get(pk=pk)
        serializer = ToDoListSerializer(todo)
        return Response(serializer.data)

    #update specific to do
    def put(self, request, pk):
        print("Executing APIView put object...")
        todo = to_do_list.objects.get(pk=pk)
        serializer = ToDoListSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    #delete specific to do
    def delete(self, request, pk):
        print("Executing APIView delete...")
        to_do_list.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    #complete to do
    def completeTodo(self, request, pk):
        print("Executing APIView complete....")
        todo = to_do_list.objects.get(pk=pk)
        todo.complete = True
        todo.save()