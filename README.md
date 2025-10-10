# 🚗 Análise da Taxa de Mortalidade no Trânsito - Estado do Rio de Janeiro

Este projeto tem como objetivo analisar a **evolução da taxa de mortalidade no trânsito** no Estado do Rio de Janeiro, utilizando dados públicos disponibilizados pelo portal **[DATA RIO](https://www.data.rio/)**.  
A análise busca compreender as tendências históricas, identificar fatores associados a picos e quedas nos índices e oferecer uma base sólida para estudos futuros sobre segurança viária.

---

## 📊 Objetivos do Projeto

- Realizar a leitura e padronização de várias abas de um arquivo Excel contendo dados de mortalidade no trânsito.  
- Limpar os dados, removendo inconsistências e valores inválidos (como `...`).  
- Analisar a **distribuição de frequência** dos óbitos e da taxa de mortalidade.  
- Aplicar uma **Regressão Linear Simples** para identificar tendências históricas.  
- Gerar **estatísticas descritivas** que resumem a evolução da mortalidade no trânsito ao longo dos anos.

---

## 🧠 Metodologia

O pipeline desenvolvido realiza as seguintes etapas:

1. **Leitura dos dados** – Carregamento de múltiplas abas do arquivo Excel.  
2. **Limpeza e padronização** – Remoção de inconsistências e normalização dos dados.  
3. **Análise exploratória** – Avaliação da distribuição dos óbitos e da taxa de mortalidade.  
4. **Modelagem estatística** – Aplicação de Regressão Linear Simples para identificar tendências temporais.  
5. **Síntese de resultados** – Interpretação e contextualização dos principais achados.

---

## 📈 Principais Resultados e Interpretações
- **Entre 2000 e 2006**, as taxas se mantiveram elevadas, com grande variação anual.  
  A partir de **2007**, houve **redução significativa**, reflexo do fortalecimento das leis de trânsito.
- **2012 e 2014** apresentaram os maiores números de óbitos.  
  - Em **2012**, a maior taxa de mortalidade foi entre pedestres. A queda nos anos seguintes se deve à ampliação da **Lei Seca**, que reduziu acidentes causados por motoristas alcoolizados.  
  - Em **2014**, o aumento é atribuído à **Copa do Mundo**, evento que trouxe intenso fluxo de turistas e maior movimentação nas vias.  
  - Em **2015**, observa-se uma **queda acentuada** nos óbitos, resultado das melhorias viárias realizadas para o evento anterior.  
  - Em **2016**, ocorre nova elevação devido às **Olimpíadas**, outro evento de grande porte sediado na cidade.  
- **Após 2017**, há um leve aumento gradual nas taxas, possivelmente ligado à **popularização de aplicativos de transporte e entrega** (Uber, iFood, etc.), que aumentaram a circulação de veículos, motos e bicicletas.  
  Ainda assim, os números se mantêm abaixo dos picos anteriores, em parte pela expansão das **ciclovias** no estado.


---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Pandas** – Leitura e manipulação de dados
- **Matplotlib / Seaborn** – Visualização gráfica
- **Scikit-learn** – Regressão Linear
- **Jupyter Notebook** (ou VS Code) – Ambiente de desenvolvimento

---


---

## 📚 Fonte dos Dados

- **Portal DATA RIO:** (https://www.data.rio/)(https://www.data.rio/documents/874f371df3084631b41dbb9c9d31ba50/about))  
  *Base: Taxa de Mortalidade no Trânsito - Estado do Rio de Janeiro.*

---

## 💬 Conclusão

A análise evidencia que as variações nas taxas de mortalidade no trânsito estão fortemente relacionadas a **mudanças nas políticas públicas**, **grandes eventos** e **mudanças no comportamento urbano**.  
A metodologia aplicada oferece uma base sólida para **futuras análises preditivas** e **estudos de impacto de políticas de mobilidade e segurança viária**.

---

## 👨‍💻 Autor

**Hiago Gonçalves de Souza**  
📧 Contato: *souza.hgs@outlook.com*  
🔗 GitHub: [https://github.com/hiaguin-dev]





