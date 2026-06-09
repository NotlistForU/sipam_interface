import json
from django.views import View
from django.shortcuts  import render, get_list_or_404
from django.http import HttpResponse, JsonResponse
from sipam_interface.sipam_inundacao_urbana.inundacao_urbana import InundacaoUrbana
from .inundacao_urbana_service import InundacaoUrbanaService

class InundacaoUrbanaCadastroView(View):
     """Controller responsável apenas pela tela e ação de cadastro"""

     def get(self, request) -> HttpResponse:
          return render(request,'cadastro_dados.html', {'titulo': 'Cadastro de Inundação Urbana'})

     def post(self, request) -> JsonResponse:
          dados = json.loads(request.body)
          novo_registro = InundacaoUrbana.objects.create(
               municipio = dados.get('municipio'),
               #....
          )
          return JsonResponse({'mensagem': 'Cadastrado com sucesso!'})
     

class InundacaoUrbanaListagemDadosView(View):
     """Controller responsável pela listagem dados"""

     def get(self, request) -> HttpResponse:
          service = InundacaoUrbanaService()
          registros = service.listar_todos_dados()
          return render(request, 'listagem_dados.html', {'registros': registros})
# lisagem_dados():
#   if request.method == 'GET:
#       registros = service.listagem_dados()
#


# cadastro_dados():
#   if request.method == 'POST':
#       dados_reqisicao = json.loads(request.body)
#       novo_registro = services.cadastro_dados(dados_requisicao);
#       return JsonResponse({'mensagem': 'Cadastrado', 'id': novo_registro.id}, status=201)
#   



# edicao_dados():
#   registro = InundacaoUrbana.objects.get(id=1);
#   registro.municipio = "Novo Valor";
#   registro.save();
#

# exclusao():
#   registro = InundacaoUrbana.objects.get(id=1);
#   registro.status = False;
#


