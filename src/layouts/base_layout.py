import src.layouts.layout_enum as layout_enum

from dataclasses import dataclass, field, fields, Field
from typing import List, Optional

@dataclass
class BaseLayout:

    @staticmethod
    def get_layout() -> layout_enum.LayoutEnum:
        """
        Enum correnspondente ao Layout que será identificado no 'retorno_serasa'
        """
        raise NotImplementedError('Método GetLayout deve ser implementado')

    secao: Optional[dict] = field(default=None)

    def __post_init__(self):
        if self.secao is not None:
            self.mapear()

    def retorna_campos_mapeaveis(self) -> List[Field]:
        """
        Método responsável por retornar a lista de campos mapeáveis
        """
        field_list = fields(self)
        return_list = []
        for field in field_list:
            if field.metadata is not None and 'mapping_field' in field.metadata and field.metadata['mapping_field']:
                return_list.append(field)

        return return_list

    def mapear(self):
        raise NotImplementedError('Método mapear não está implementado no layout')

    def mapear_linha(self, linha):
        fields_contabilizacao = self.retorna_campos_mapeaveis()
        for field in fields_contabilizacao:
            inicio = field.metadata['start']
            if inicio > 0:
                inicio = inicio -1
            fim = inicio + field.metadata['len']
            setattr(self, field.name, linha[inicio:fim])

    def mapear(self):
        raise NotImplementedError('Método mapear não implementado')
        
