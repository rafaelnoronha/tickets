from rest_framework import viewsets, mixins
from .models import Usuario, LogAutenticacao
from .serializer import UsuarioSerializer, UsuarioSerializerCreate, UsuarioSerializerRetrieve,\
                        LogAutenticacaoSerializer, LogAutenticacaoSerializerRetrieve


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    lookup_field = 'uuid'

    serializer_classes = {
        'create': UsuarioSerializerCreate,
        'retrieve': UsuarioSerializerRetrieve,
    }

    def get_serializer_class(self):
        print(self.action)
        return self.serializer_classes.get(self.action, UsuarioSerializer)


class LogAutenticacaoViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    queryset = LogAutenticacao.objects.all()
    lookup_field = 'uuid'

    serializer_classes = {
        'retrieve': LogAutenticacaoSerializerRetrieve
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, LogAutenticacaoSerializer)
