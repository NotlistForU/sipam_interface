from sipam_interface.sipam_inundacao_urbana.inundacao_urbana import InundacaoUrbana

class InundacaoUrbanaRepositry:

    def __init__(self, entity = InundacaoUrbana):
        self.entity = entity

    def listar_todos_dados(self):
        dados = self.entity.objects.all()
        return dados

