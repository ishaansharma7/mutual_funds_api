from django.db import models
from django.db.models import fields
from rest_framework import serializers
from basic_app.models import MutualFundsScheme, MutualFundsCode

class MutualFundsSchemeSerializer(serializers.ModelSerializer):
    scheme_code = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = MutualFundsScheme
        fields = '__all__'

class MutualFundsCodeSerializer(serializers.ModelSerializer):

    # mutual_funds_schemes = serializers.HyperlinkedRelatedField(many=True,read_only=True, view_name='scheme-detail')

    class Meta:
        model = MutualFundsCode
        fields = '__all__'