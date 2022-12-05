from dataclasses import dataclass, field
from typing import List

from src.layouts.contabilizacao import Contabilizacao

@dataclass
class MapeamentoSerasaPJ:
    
    retorno_serasa:str
    secoes: dict = field(init=False)
    contabilizacao: Contabilizacao = field(init=False, default=None)

    def __post_init__(self):
        self.identificar_layouts()

    def identificar_layouts(self):
        """
        Método responsável por identificar cada layout no retorno do serasa
        """
        layouts = self.retorno_serasa.split('#L')
        self.secoes = {}
        for layout in layouts:
            chave = layout[:6]
            if chave not in self.secoes:
                self.secoes[chave] = []
            self.secoes[chave].append(layout[6:])

    def iniciar_mapeamento(self):
        self.contabilizacao = Contabilizacao(self.secoes[Contabilizacao.get_layout().value])