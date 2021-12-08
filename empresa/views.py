from rest_framework import viewsets
from .models import Empresa
from .serializer import EmpresaSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    lookup_field = 'uuid'
    serializer_class = EmpresaSerializer
