
from rest_framework import serializers
from predicteur_app.models import Individu


class IndividuSerializer(serializers.Serializer):

    ChestACCX = serializers.FloatField()
    ChestACCY = serializers.FloatField()
    ChestACCZ = serializers.FloatField()
    ChestECG = serializers.FloatField()
    ChestResp = serializers.FloatField()
    WristACCX = serializers.FloatField()
    WristACCY = serializers.FloatField()
    WristACCZ = serializers.FloatField()
    WristBVP = serializers.FloatField()
    Weight = serializers.FloatField()
    Gender = serializers.FloatField()
    Age = serializers.FloatField()
    Height = serializers.FloatField()
    Sport = serializers.FloatField()
    #y to predict
    activity = serializers.FloatField(allow_null=True)

    def create(self, validated_data):
        return Individu.objects.create(**validated_data)