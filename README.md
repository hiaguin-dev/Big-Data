# 📊 Análise de Dados de Mortalidade

Este projeto realiza **análise exploratória** e **modelagem estatística** (Regressão Linear) sobre dados de mortalidade contidos em planilhas Excel.
Ele automatiza a leitura de múltiplas abas, faz a limpeza dos dados, gera gráficos descritivos e apresenta métricas estatísticas de tendência temporal.

---

## 🚀 Funcionalidades

* Leitura automática de **todas as abas** de um arquivo Excel (.xlsx)
* Limpeza e padronização dos dados (remoção de colunas inválidas e tratamento de nomes)
* Análise exploratória com gráficos:

  * Distribuição de óbitos
  * Evolução temporal dos óbitos
  * Boxplot
  * Distribuição da taxa de mortalidade
* Aplicação de **Regressão Linear** para identificar tendência dos óbitos ao longo dos anos
* Cálculo de métricas estatísticas (R², RMSE, média, desvio padrão, coeficiente de variação)
* Geração de arquivo final com dados limpos (`dados_processados.xlsx`)

---

## 🧠 Estrutura do Código

O script é dividido em quatro partes principais:

1. **Leitura dos Dados (`ler_dados_excel`)**

   * Percorre todas as abas do Excel.
   * Renomeia colunas para um formato padronizado.
   * Filtra apenas colunas relevantes (`ano`, `obitos`, `populacao`, `taxa`).
   * Trata valores inválidos e converte tipos de dados.

2. **Análise Exploratória (`analise_exploratoria`)**

   * Exibe estatísticas descritivas dos dados.
   * Gera visualizações para compreender a distribuição e a evolução temporal.

3. **Regressão Linear (`analise_regressao`)**

   * Ajusta um modelo linear simples entre `ano` e `óbitos`.
   * Exibe a equação, o valor de R², o erro médio quadrático (RMSE) e a tendência (crescente ou decrescente).
   * Mostra o gráfico de regressão com pontos observados e previsão para anos futuros.

4. **Execução Principal (`main`)**

   * Define o arquivo Excel de entrada (`3124.xlsx`).
   * Integra todas as etapas de leitura, análise e exportação.
   * Salva o resultado final em `dados_processados.xlsx`.

---

## 📦 Requisitos

Certifique-se de ter instalado as seguintes bibliotecas:

```bash
pip install pandas matplotlib seaborn scikit-learn openpyxl numpy
```

---

## ▶️ Como Executar

1. Coloque o arquivo `3124.xlsx` na mesma pasta do script.
2. Execute o script com Python:

```bash
python nome_do_arquivo.py
```

3. O terminal exibirá mensagens de progresso, estatísticas e resultados.
4. Ao final, o arquivo `dados_processados.xlsx` será gerado com os dados tratados.

---

## 📈 Exemplo de Saída

Durante a execução, o script exibe:

```
🚀 Iniciando análise de dados de mortalidade...
✅ Aba 'Região Norte': 15 linhas válidas
✅ Aba 'Região Sul': 20 linhas válidas
✅ Base final criada com 35 registros
📊 ANÁLISE EXPLORATÓRIA COMPLETA
📈 REGRESSÃO LINEAR - RESULTADOS
Equação: Óbitos = 123.45 * Ano + 67890.12
R² = 0.972
RMSE = 45.21
Tendência: CRESCENTE
```

Além disso, gráficos interativos serão exibidos com as distribuições e regressões.

---

## 🗂️ Saídas Geradas

* **Gráficos:** exibidos em tela (Matplotlib/Seaborn)
* **Arquivo final:** `dados_processados.xlsx`
* **Resumo estatístico:** impresso no console

---

## 🧩 Tecnologias Utilizadas

* **Python 3.8+**
* **Pandas** — manipulação e limpeza de dados
* **Matplotlib & Seaborn** — visualização gráfica
* **Scikit-learn** — regressão linear e métricas
* **NumPy** — operações numéricas

---

## 🧑‍💻 Autor

**Hiago Gonçalves de Souza**
Projeto de análise automatizada de dados de mortalidade — aprendizado, visualização e modelagem estatística com Python.

---





