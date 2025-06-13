 # Parte 2: análise dos depósitos

import pandas as pd

def main():
    # 1) Carrega a planilha
    df = pd.read_excel('Análise de Dados.xlsx')

    # 2) Quantos depósitos cada máquina recebeu?
    #    Agrupa por ID MÁQUINA e conta linhas
    depositos_por_maquina = (
        df.groupby('ID MÁQUINA')
          .size()
          .rename('Depósitos')
          .reset_index()
    )

    # 3) Quantos pontos foram distribuídos no total?
    pontos_totais = df['PONTOS'].sum()

    # 4) Exibe resultados
    print('Depósitos por máquina:')
    print(depositos_por_maquina.to_string(index=False))

    print(f'\nPontos totais distribuídos: {pontos_totais}')

if __name__ == '__main__':
    main()
