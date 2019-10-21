from django.conf.urls import url
try:
  from django.conf.urls import patterns
except ImportError:
  pass
import django
from projeto import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API REST SERVICENET')

urlpatterns = [

  url(r'^autenticacao/(?P<id>[0-9]+)$', views.AutenticacaoManupularAPIView.as_view()),
  url(r'^autenticacao/$', views.AutenticacaoAPIView.as_view()),
  url(r'^autenticacao/login/$', views.LoginAPIView.as_view()),

  url(r'^cliente/(?P<id>[0-9]+)$', views.ClienteAPIView.as_view()),
  url(r'^cliente/$', views.ClienteAPIListView.as_view()),

  url(r'^docs/', schema_view),

]
