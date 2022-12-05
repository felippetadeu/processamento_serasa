def retorna_retorno_serasa() -> str:
    import os
    retorno_serasa = ''
    with open(os.path.join(os.getcwd(), 'retorno_serasa.txt'), encoding='utf8') as file:
        retorno_serasa = file.readlines()[0]
    retorno_serasa = retorno_serasa.replace('\xa0', ' ').replace('#BLC', '')
    
    return retorno_serasa


def main():
    from src.layouts.mapeamento_serasa_pj import MapeamentoSerasaPJ
    retorno_serasa = retorna_retorno_serasa()
    mapeamento = MapeamentoSerasaPJ(retorno_serasa=retorno_serasa)
    mapeamento.iniciar_mapeamento()
    if mapeamento.contabilizacao is not None:
        print(mapeamento)


if __name__ == '__main__':
    main()