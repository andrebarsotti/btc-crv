# Desafio Prático - Módulo 2: Coleta e Armazenamento de Dados em Renda Variável

## Objetivos de Ensino

Exercitar os seguintes conceitos trabalhados no Módulo:

1. Implementar processos para coleta e armazenamento de dados em Renda Variável usando a linguagem Python;
2. Reconhecer e explorar fontes de dados públicas;
3. Seguir boas práticas de programação ao coletar dados da web.

## Enunciado

Continuando nosso exemplo do Trabalho Prático, agora o gestor de portfólio de ações nos solicitou adicionarmos alguns outros dados à nossa análise de
Ambev (ABEV3). Dessa vez, adicionalmente aos dados de mercado e aos dados macroeconômicos já coletados e armazenados, ele gostaria de trazer dados
fundamentalistas para o relatório de análise. 

## Atividades

1. Colete e processe os ITRs de Ambev para o período de 2019-2022, utilizando o sistema RAD CVM como fonte de dados (lembre-se que para realizarmos a consulta precisamos saber o código CVM da companhia);
2. Armazene esses dados fundamentalistas em um banco de dados relacional SQL local ou em nuvem;
3. Leia essa série histórica do banco de dados SQL usando o Python;
4. Filtre apenas os dados de “Receita de Venda de Bens e/ou Serviços” dentro da “Demonstração do Resultado” do “DFs Consolidadas”;
5. Gere um pandas DataFrame final apenas com esses valores de “Receita de Venda de Bens e/ou Serviços” e a respectiva data;
6. É essa tabela que estamos interessados. Salve-a localmente num arquivo Excel com formato .xlsx.