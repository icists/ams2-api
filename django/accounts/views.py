from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from django_countries import countries

from .models import School
from .serializers import SchoolSerializer, CountrySerializer, UserSerializer


class SchoolList(ListAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        queryset = School.objects.all()
        query = self.request.query_params.get('query', None)
        if query is not None:
            queryset = queryset.filter(name__icontains=query)
        return queryset.order_by('name')[:50]


class CountryList(ListAPIView):
    serializer_class = CountrySerializer
    queryset = [{'code': code, 'name': name} for code, name in list(countries)]


class UserView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }
