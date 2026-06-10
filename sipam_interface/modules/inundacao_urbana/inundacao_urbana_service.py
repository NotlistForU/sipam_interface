from sipam_interface.modules.inundacao_urbana.inundacao_urbana_repository import InundacaoUrbanaRepository

class InundacaoUrbanaService:

    def __init__(self, repository = InundacaoUrbanaRepository()):
        self.repository = repository

    
    def listar_todos_dados(self):
        return self.repository.listar_todos_dados()


# lisagem_dados():
#   registro = InundacaoUrbana.objects.all()
#
#


# cadastro_dados():
#   registro = InundacaoUrbana(
#       cd_geocodi='1234567891011121314',
#       municipio=...
# 
#   registro.save();



# edicao_dados():
#   registro = InundacaoUrbana.objects.get(id=1);
#   registro.municipio = "Novo Valor";
#   registro.save();
#

# exclusao():
#   registro = InundacaoUrbana.objects.get(id=1);
#   registro.status = False;
#

