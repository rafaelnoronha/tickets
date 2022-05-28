from rest_framework import viewsets, mixins
from core.views import ModelViewSetComAuditoria, CreateModelMixinAuditoria
from .models import Ticket, MensagemTicket
from .filters import TicketFilter, MensagemTicketFilter
from core.permissions import BasePemission
from .serializer import TicketSerializer, TicketSerializerRetrieve, TicketSerializerCreate, TicketSerializerUpdatePartialUpdate, \
                        MensagemTicketSerializer, MensagemTicketSerializerCreate, MensagemTicketSerializerRetrieve, \
                        TicketSerializerAuditoria, MensagemTicketSerializerAuditoria


class TicketViewSet(ModelViewSetComAuditoria):
    queryset = Ticket.objects.all()
    lookup_field = 'uuid'
    filterset_class = TicketFilter
    permission_classes = (BasePemission, )
    auditoria = {
        'modelo': Ticket,
        'nome_tabela': 'ticket',
        'serializer': TicketSerializerAuditoria,
    }

    serializer_classes = {
        'retrieve': TicketSerializerRetrieve,
        'create': TicketSerializerCreate,
        'update': TicketSerializerUpdatePartialUpdate,
        'partial_update': TicketSerializerUpdatePartialUpdate,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, TicketSerializer)


class MensagemTicketViewSet(CreateModelMixinAuditoria, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    queryset = MensagemTicket.objects.all()
    lookup_field = 'uuid'
    filterset_class = MensagemTicketFilter
    permission_classes = (BasePemission, )
    auditoria = {
        'modelo': MensagemTicket,
        'nome_tabela': 'mensagem_ticket_serializer',
        'serializer': MensagemTicketSerializerAuditoria,
    }

    serializer_classes = {
        'create': MensagemTicketSerializerCreate,
        'retrieve': MensagemTicketSerializerRetrieve,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, MensagemTicketSerializer)
