import src.layouts.layout_enum as layout_enum

from dataclasses import dataclass, field
from src.layouts.base_layout import BaseLayout

@dataclass
class Contabilizacao(BaseLayout):
    @staticmethod
    def get_layout() -> layout_enum.LayoutEnum:
        return layout_enum.LayoutEnum.CONTABILIZACAO

    idinf: str = field(init=False, default=None, metadata={'mapping_field': True, 'start':1, 'len': 2})
    """
    id inf: 01 - cadastral - INIC 01 TAM 02 TIPO N
    """

    bcfic: str = field(init=False, default=None, metadata={'mapping_field': True, 'start':3, 'len': 2})
    """
    bloco: 00 - controle - INIC 03 TAM 02 TIPO N
    """

    tpinf: str = field(init=False, default=None, metadata={'mapping_field': True, 'start':5, 'len': 2})
    """
    tp inf: 00 - dados da ficha cadastral - INIC 05 TAM 02 TIPO N
    """

    cdsitrf: str = field(init=False, default=None, metadata={'mapping_field': True, 'start':7, 'len': 2})
    """
    descrição da situação da empresa - INIC 07 TAM 02 TIPO N
    """

    dssitrf: str = field(init=False, default=None, metadata={'mapping_field': True, 'start':9, 'len': 79})
    """
    código cnpj consultado - INIC 09 TAM 79 TIPO C
    """

    cdcg: str = field(init=False, default=None, metadata={'mapping_field': True, 'start':88, 'len': 9})
    """
    indicador se tem ficha - INIC 88 TAM 09 TIPO N
    """

    indficha: str = field(init=False, default=None, metadata={'mapping_field': True, 'start':97, 'len': 1})
    """
    indicador se tem ficha - INIC 97 TAM 01 TIPO C
    """

    trn_contab: str = field(init=False, default=None, metadata={'mapping_field': True, 'start':98, 'len': 4})
    """
    transação contabilizada - INIC 98 TAM 04 TIPO C
    """

    cdmsgrecipr: str = field(init=False, default=None, metadata={'mapping_field': True, 'start':102, 'len': 1})
    """
    código da mensagem de reciprocidade - INIC 102 TAM 01 TIPO C
    """

    dtultrecipr: str = field(init=False, default=None, metadata={'mapping_field': True, 'start':103, 'len': 10})
    """
    data última remessa de reciprocidade - INIC 103 TAM 10 TIPO C
    """

    trn_cont02: str = field(init=False, default=None, metadata={'mapping_field': True, 'start':113, 'len': 4})
    """
    transação contabilizada desmembrada 02 - INCI 113 TAM 04 TIPO C
    """

    trn_cont03: str = field(init=False, default=None)
    """
    transação contabilizada desmembrada 03 - INCI 117 TAM 04 TIPO C
    """

    trn_cont04: str = field(init=False, default=None)
    """
    transação contabilizada desmembrada 04 - INCI 121 TAM 04 TIPO C
    """

    trn_cont05: str = field(init=False, default=None)
    """
    transação contabilizada desmembrada 05 - INCI 125 TAM 04 TIPO C
    """

    trn_cont06: str = field(init=False, default=None)
    """
    transação contabilizada desmembrada 06 - INCI 129 TAM 04 TIPO C
    """

    trn_cont07: str = field(init=False, default=None)
    """
    transação contabilizada desmembrada 07 - INCI 133 TAM 04 TIPO C
    """

    trn_cont08: str = field(init=False, default=None)
    """
    transação contabilizada desmembrada 08 - INCI 137 TAM 04 TIPO C
    """

    trn_cont09: str = field(init=False, default=None)
    """
    transação contabilizada desmembrada 09 - INCI 141 TAM 04 TIPO C
    """

    trn_cont10: str = field(init=False, default=None)
    """
    transação contabilizada desmembrada 10 - INCI 145 TAM 04 TIPO C
    """

    tiprelato: str = field(init=False, default=None)
    """
    tipo de relato: 10analítico 2-sintético - INIC 149 TAM 01 TIPO C
    """

    temrecipr: str = field(init=False, default=None)
    """
    tem reciprocidade: s | n - INIC 150 TAM 01 TIPO C
    """

    tiprelcob: str = field(init=False, default=None)
    """
    1=quadro social cortesia 2=cobra quadro social - INIC 151 TAM 01 TIPO C
    """

    diasrest: str = field(init=False, default=None)
    """
    Quantidade de dias restantes para Liberação Automática de Visão Analítica.
    Quando o código da mensagem de reciprocidade for igual "E"
     - INIC 152 TAM 02 TIPO N
    """

    cdsitunov: str = field(init=False, default=None)
    """
    Código da Situação Cadastral (Novo)
    0 - Inapta
    1 - Ativa
    2 - Nula
    4 - Suspensa
    7 - Baixada
    - INIC 154 TAM 01 TIPO N
    """

    dssitunov: str = field(init=False, default=None)
    """
    Descrição da situação cadastral (Novo) - INIC 155 TAM 80 TIPO C
    """

    data_aviso_previo: str = field(init=False, default=None)
    """
    DAta aviso prévio - INIC 235 TAM 10 TIPO C
    """

    tem_prot_indis: str = field(init=False, default=None)
    """
    Tem protesto indisponível S | N - INIC 240 TAM 01 TIPO C
    """
    
    def mapear(self):
        linha = self.secao[0]
        linha = Contabilizacao.get_layout().value + linha
        self.mapear_linha(linha)