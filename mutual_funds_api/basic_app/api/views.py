from rest_framework.generics import ListAPIView, RetrieveAPIView
from basic_app.api.serializers import MutualFundsSchemeSerializer, MutualFundsCodeSerializer
from basic_app.models import MutualFundsScheme, MutualFundsCode
from basic_app.api.pagination import SmallSetPagination
from rest_framework.response import Response

class MutualFundsSchemeListAPIView(ListAPIView):
    queryset = MutualFundsScheme.objects.all()
    serializer_class = MutualFundsSchemeSerializer
    pagination_class = SmallSetPagination

class MutualFundsCodeListAPIView(ListAPIView):
    queryset = MutualFundsCode.objects.all()
    serializer_class = MutualFundsCodeSerializer
    pagination_class = SmallSetPagination

    