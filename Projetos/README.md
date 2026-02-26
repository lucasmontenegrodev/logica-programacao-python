Sistema de Periodização e Cálculo de Carga Máxima (1RM)
Este projeto consiste em uma ferramenta de terminal desenvolvida em Python para auxiliar no planejamento de treinamentos de força. O sistema automatiza o cálculo de 1RM (uma repetição máxima) e gera estruturas de periodização baseadas em modelos metodológicos aplicados à musculação.

Escopo Técnico
O software foi estruturado para resolver o problema da progressão de carga através de:

Cálculos Multimetodológicos: Implementação das fórmulas de Epley, Brzycki, Lombardi e O'Conner para estimativa de carga máxima.

Algoritmos de Periodização: Geração de planos de treino baseados em modelos lineares, ondulatórios ou em blocos, com ajustes automáticos de volume e intensidade.

Persistência de Dados: Utilização de arquivos JSON para o armazenamento e recuperação do histórico de treinos do usuário.

Módulo de Exportação: Função para gerar relatórios detalhados em formato de texto (.txt) para consulta externa.

Estrutura do Código
O script utiliza funções modulares para garantir a validação de entradas de dados (limpeza de strings e conversão de tipos), tratamento de erros em tempo de execução e manipulação de arquivos locais.

Instruções de Uso
Certifique-se de ter o Python 3 instalado em seu ambiente.

Execute o comando: python 1rmv2.py.

Utilize o menu numérico para navegar entre as funções de configuração de plano, consulta de histórico ou cálculos avulsos.