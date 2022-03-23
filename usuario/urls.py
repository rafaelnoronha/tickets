from rest_framework.routers import SimpleRouter
from .views import UsuarioViewSet, LogAutenticacaoViewSet, GrupoPermissoesUsuarioViewSet, PermissaoUsuarioViewSet

router_usuario = SimpleRouter()
router_usuario.register('', UsuarioViewSet)

router_log_autenticacao = SimpleRouter()
router_log_autenticacao.register('', LogAutenticacaoViewSet)

router_grupo_permissoes_usuario = SimpleRouter()
router_grupo_permissoes_usuario.register('', GrupoPermissoesUsuarioViewSet)

router_permissao_usuario = SimpleRouter()
router_permissao_usuario.register('', PermissaoUsuarioViewSet)
