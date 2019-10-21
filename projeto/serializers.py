from rest_framework.serializers import ModelSerializer
from projeto.models import Autenticacao, Cliente


class AutenticacaoSerializer(ModelSerializer):

    class Meta:
        model = Autenticacao
        fields = ['nome']


class ClienteSerializer(ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'
