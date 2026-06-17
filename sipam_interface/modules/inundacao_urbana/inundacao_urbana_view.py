import json
from django.views import View
from django.shortcuts  import render, get_list_or_404
from django.http import HttpResponse, JsonResponse
from sipam_interface.modules.inundacao_urbana.inundacao_urbana_model import InundacaoUrbana

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
          return JsonResponse(request, novo_registro, {'mensagem': 'Cadastrado com sucesso!'})
     

class InundacaoUrbanaListagemDadosView(View):
     """Controller responsável pela listagem dados"""

     def get(self, request) -> HttpResponse:
          dados = InundacaoUrbana.objects.all();

          num_dados = len(dados)
          num_estacoes = sum(1 for item in dados if item.cd_estacao)
          num_municipios = len(set(item.municipio for item in dados))

          num_integrado = sum(1 for item in dados if item.integrado)
          num_cota_atencao = sum(1 for item in dados if item.cota_atencao)
          num_cota_alerta = sum(1 for item in dados if item.cota_alerta)
          num_cota_inundacao = sum(1 for item in dados if item.cota_inundacao)

          
          
          if num_dados > 0 :
               por_cent_integrado = (num_integrado * 100) / num_dados
          else:
               por_cent_integrado = 0.0

          return render(
               request, 'componentes/index.html', 
                        {
                             'dados': dados,
                             'num_dados': num_dados, 
                             'num_municipios': num_municipios,
                             'num_estacoes': num_estacoes,
                             'num_integrado': num_integrado,
                             'num_cota_atencao': num_cota_atencao,
                             'num_cota_alerta': num_cota_alerta,
                             'num_cota_inundacao': num_cota_inundacao,
                             'por_cent_integrado': por_cent_integrado})


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


