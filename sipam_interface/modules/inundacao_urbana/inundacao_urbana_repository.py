from sipam_interface.modules.inundacao_urbana.inundacao_urbana_entity import InundacaoUrbana

class InundacaoUrbanaRepository:

    def __init__(self, entity = None):
        self.entity = entity or InundacaoUrbana

    def listar_todos_dados(self):
        dados = self.entity.objects.all()
        return dados

