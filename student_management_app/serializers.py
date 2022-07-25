from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('id', 'gender', 'profile_pic', 'course_id')
