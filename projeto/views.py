from rest_framework.response import Response
from rest_framework.views import APIView

from projeto.serializers import AutenticacaoSerializer, ClienteSerializer
from projeto.models import Autenticacao, Cliente

class AutenticacaoManupularAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = Autenticacao.objects.get(pk=id)
            serializer = AutenticacaoSerializer(item)
            return Response(serializer.data)
        except Autenticacao.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Autenticacao.objects.get(pk=id)
        except Autenticacao.DoesNotExist:
            return Response(status=404)
        serializer = AutenticacaoSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Autenticacao.objects.get(pk=id)
        except Autenticacao.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AutenticacaoAPIView(APIView):
    def post(self, request, format=None):
        serializer = AutenticacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def get(self, request, format=None):
        items = Autenticacao.objects.all()
        serializer = AutenticacaoSerializer(items)
        return Response(serializer.data, status=200)


class LoginAPIView(APIView):
    def post(self, request, format=None):
        try:
            email = Autenticacao.objects.get(email=request.POST['email'])
            password = Autenticacao.objects.get(password=request.POST['password'])

            if email is not None and password is not None:
                serializer = AutenticacaoSerializer(email)
                return Response(serializer.data, status=200)
            return Response(False, status=400)

        except Autenticacao.DoesNotExist:
            return Response(False, status=404)



class ClienteAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = Cliente.objects.get(pk=id)
            serializer = ClienteSerializer(item)
            return Response(serializer.data)
        except Cliente.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Cliente.objects.get(pk=id)
        except Cliente.DoesNotExist:
            return Response(status=404)
        serializer = ClienteSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Cliente.objects.get(pk=id)
        except Cliente.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ClienteAPIListView(APIView):
    def get(self, request, format=None):
        items = Cliente.objects.all()
        serializer = ClienteSerializer(items, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)
