# Trabalho Prático - Módulo 2: Coleta e Armazenamento de Dados em Renda Variável

## Objetivos de Ensino

Exercitar os seguintes conceitos trabalhados no Módulo:

1. Implementar processos para coleta e armazenamento de dados em Renda Variável, usando a linguagem Python;
2. Reconhecer e explorar fontes de dados públicas;
3. Seguir boas práticas de programação ao coletar dados da web.

## Enunciado

Suponha que trabalhamos em uma gestora de fundos de investimentos e o gestor de portfólio de ações nos solicitou apresentar dados que possam ajudá-lo a decidir investir ou não em Ambev (ABEV3). 

Em particular, ele gostaria de olhar dados de mercado, dados fundamentalistas, dados macroeconômicos e dados alternativos em um relatório bastante minucioso.

Inicialmente ele nos solicitou apenas os dados de mercado e dados macroeconômicos para iniciar nossa análise.

## Atividades

1. [x] Colete a série histórica dos dados de inflação de bebidas do IBGE usando a API sidra;
2. [x] Colete a série histórica dos dados diários de preços e volume (OHLCV) para a ação ABEV3 do provedor de sua preferência (yahoo, finance, marketstack, eodhistoricaldata, finnhub, alphavantage, etc.);
3. [x] Crie e armazene esses dados em um banco de dados SQL local ou em nuvem;
4. [ ] Esboce como seria a implementação em Python de uma DAG Airflow, que executaria as coletas implementadas anteriormente. O código não precisa rodar com sucesso, é apenas um esboço.

