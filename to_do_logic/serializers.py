from to_do_logic.models import to_do_list
from django.contrib.auth import authenticate
from rest_framework import serializers

#create serializer
class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = to_do_list
        fields = ('title', 'description', 'due_date', 'priority')
