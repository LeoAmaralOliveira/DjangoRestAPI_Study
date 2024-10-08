from school.models import Student, Course, Registration
from school.serializers import (
    StudentSerializer,
    StudentSerializerV2,
    CourseSerializer,
    RegistratioSerializer,
    ListRegistrationsStudentSerializer,
    ListRegistrationsCourseSerializer
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf',]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RegistrationViewSet(ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistratioSerializer


class ListRegistrationStudent(ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(student=self.kwargs['pk'])
        return queryset

    serializer_class = ListRegistrationsStudentSerializer


class ListRegistrationCourse(ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(course=self.kwargs['pk'])
        return queryset

    serializer_class = ListRegistrationsCourseSerializer
