import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# ===== 1. Ler o arquivo Excel =====
arquivo = "3124.xlsx"
xls = pd.ExcelFile(arquivo)

tabelas = []

for aba in xls.sheet_names:
    try:
        df = pd.read_excel(arquivo, sheet_name=aba, skiprows=4, engine="openpyxl")

        if df.empty:
            print(f"Aba {aba} está vazia, pulando...")
            continue

        # padronizar nomes das colunas
        df.columns = df.columns.str.strip().str.lower()

        # renomear colunas conhecidas
        df = df.rename(columns={
            "ano": "ano",
            "óbitos": "obitos",
            "óbito": "obitos",
            "população": "populacao",
            "populacao": "populacao",
            "taxa de mortalidade": "taxa",
            "taxa de mortalidade por 100 mil hab.": "taxa"
        })

        # manter apenas colunas de interesse
        colunas_necessarias = ["ano", "obitos", "populacao", "taxa"]
        df = df[[c for c in colunas_necessarias if c in df.columns]]

        if not df.empty:
            tabelas.append(df)

    except Exception as e:
        print(f"Erro na aba {aba}: {e}")

# ===== 2. Concatenar e limpar =====
if len(tabelas) == 0:
    raise ValueError("Nenhuma aba válida foi encontrada no Excel.")

df_final = pd.concat(tabelas)

# converter colunas para numérico (se existirem)
for col in ["ano", "obitos", "populacao", "taxa"]:
    if col in df_final.columns:
        df_final[col] = pd.to_numeric(df_final[col], errors="coerce")

# remover linhas inválidas (ano e óbitos são obrigatórios)
df_final = df_final.dropna(subset=["ano", "obitos"])
df_final["ano"] = df_final["ano"].astype(int)

print("✅ Base final criada com", len(df_final), "linhas")
print(df_final.head())

# ===== 3. Distribuição de Frequência =====
plt.figure(figsize=(10,5))
sns.histplot(df_final["obitos"], bins=10, kde=True)
plt.title("Distribuição de Frequência - Óbitos")
plt.xlabel("Óbitos")
plt.ylabel("Frequência")
plt.show()

if "taxa" in df_final.columns:
    plt.figure(figsize=(10,5))
    sns.histplot(df_final["taxa"], bins=10, kde=True, color="orange")
    plt.title("Distribuição de Frequência - Taxa de Mortalidade")
    plt.xlabel("Taxa por 100 mil hab.")
    plt.ylabel("Frequência")
    plt.show()

# ===== 4. Regressão Linear Simples =====
X = df_final[["ano"]]
y = df_final["obitos"]

modelo = LinearRegression()
modelo.fit(X, y)

y_pred = modelo.predict(X)

print("\n📈 Equação da Regressão Linear (Óbitos ~ Ano):")
print(f"Óbitos = {modelo.coef_[0]:.2f} * Ano + {modelo.intercept_:.2f}")

plt.figure(figsize=(10,6))
plt.scatter(X, y, label="Óbitos observados")
plt.plot(X, y_pred, color="red", linewidth=2, label="Linha de regressão")
plt.title("Regressão Linear Simples - Óbitos por Ano")
plt.xlabel("Ano")
plt.ylabel("Óbitos")
plt.legend()
plt.show()

# ===== 5. Resumo Estatístico =====
print("\n📊 Resumo Estatístico da base final:")
colunas_existentes = [c for c in ["obitos", "populacao", "taxa"] if c in df_final.columns]
print(df_final[colunas_existentes].describe().T)
