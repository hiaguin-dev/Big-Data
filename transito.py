import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

# ===== CONFIGURAÇÕES =====
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# ===== 1. LEITURA DO ARQUIVO =====
def ler_dados_excel(arquivo):
    """Função melhorada para leitura do arquivo Excel"""
    try:
        xls = pd.ExcelFile(arquivo)
        tabelas = []
        
        for aba in xls.sheet_names:
            try:
                df = pd.read_excel(arquivo, sheet_name=aba, skiprows=4, engine="openpyxl")
                
                if df.empty or len(df) < 2:
                    print(f"⚠️ Aba '{aba}' vazia ou com poucos dados, pulando...")
                    continue
                
                # Limpeza mais robusta dos nomes das colunas
                df.columns = (df.columns.astype(str)
                             .str.strip()
                             .str.lower()
                             .str.replace('.', '')
                             .str.replace('ó', 'o')
                             .str.replace('ç', 'c')
                             .str.replace('ã', 'a')
                             .str.replace('õ', 'o')
                             .str.replace('\s+', '_', regex=True))
                
                # Mapeamento mais abrangente de colunas
                mapeamento_colunas = {
                    'ano': 'ano',
                    'obitos': 'obitos',
                    'obito': 'obitos',
                    'populacao': 'populacao',
                    'populacao': 'populacao',
                    'taxa_mortalidade': 'taxa',
                    'taxa': 'taxa',
                    'taxa_de_mortalidade': 'taxa',
                    'taxa_de_mortalidade_por_100_mil_hab': 'taxa'
                }
                
                df = df.rename(columns=mapeamento_colunas)
                
                # Manter apenas colunas de interesse que existem
                colunas_interesse = [c for c in ["ano", "obitos", "populacao", "taxa"] 
                                   if c in df.columns]
                
                if len(colunas_interesse) < 2:  # Pelo menos ano e óbitos
                    print(f"⚠️ Aba '{aba}' não tem colunas suficientes, pulando...")
                    continue
                
                df = df[colunas_interesse]
                
                # Converter para numérico
                for col in colunas_interesse:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                
                # Remover linhas com anos ou óbitos inválidos
                df = df.dropna(subset=['ano', 'obitos'])
                df['ano'] = df['ano'].astype(int)
                
                if not df.empty:
                    df['fonte_aba'] = aba  # Identificar origem dos dados
                    tabelas.append(df)
                    print(f"✅ Aba '{aba}': {len(df)} linhas válidas")
                    
            except Exception as e:
                print(f"❌ Erro na aba '{aba}': {e}")
                continue
                
        return tabelas
        
    except Exception as e:
        print(f"❌ Erro ao ler arquivo: {e}")
        return []

# ===== 2. ANÁLISE EXPLORATÓRIA =====
def analise_exploratoria(df):
    """Análise exploratória completa dos dados"""
    
    print(f"\n{'='*50}")
    print("📊 ANÁLISE EXPLORATÓRIA COMPLETA")
    print(f"{'='*50}")
    
    # Estatísticas básicas
    print(f"Período analisado: {df['ano'].min()} - {df['ano'].max()}")
    print(f"Total de registros: {len(df)}")
    print(f"Média de óbitos: {df['obitos'].mean():.0f}")
    
    if 'taxa' in df.columns:
        print(f"Média da taxa: {df['taxa'].mean():.2f}")
    
    # Gráficos de distribuição
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Distribuição de óbitos
    sns.histplot(df["obitos"], bins=15, kde=True, ax=axes[0,0])
    axes[0,0].set_title("Distribuição de Frequência - Óbitos")
    axes[0,0].set_xlabel("Óbitos")
    axes[0,0].set_ylabel("Frequência")
    
    # Série temporal de óbitos
    if len(df) > 1:
        df_agrupado = df.groupby('ano')['obitos'].mean().reset_index()
        axes[0,1].plot(df_agrupado['ano'], df_agrupado['obitos'], marker='o', linewidth=2)
        axes[0,1].set_title("Evolução Temporal dos Óbitos")
        axes[0,1].set_xlabel("Ano")
        axes[0,1].set_ylabel("Óbitos")
        axes[0,1].grid(True, alpha=0.3)
    
    # Boxplot
    sns.boxplot(y=df["obitos"], ax=axes[1,0])
    axes[1,0].set_title("Boxplot - Óbitos")
    
    # Distribuição da taxa (se disponível)
    if "taxa" in df.columns:
        sns.histplot(df["taxa"], bins=15, kde=True, color="orange", ax=axes[1,1])
        axes[1,1].set_title("Distribuição - Taxa de Mortalidade")
        axes[1,1].set_xlabel("Taxa por 100 mil hab.")
        axes[1,1].set_ylabel("Frequência")
    
    plt.tight_layout()
    plt.show()

# ===== 3. REGRESSÃO LINEAR =====
def analise_regressao(df):
    """Análise de regressão linear com métricas"""
    
    X = df[["ano"]]
    y = df["obitos"]
    
    if len(X) < 2:
        print("❌ Dados insuficientes para regressão")
        return
    
    modelo = LinearRegression()
    modelo.fit(X, y)
    y_pred = modelo.predict(X)
    
    # Métricas
    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(np.mean((y - y_pred)**2))
    
    print(f"\n{'='*50}")
    print("📈 REGRESSÃO LINEAR - RESULTADOS")
    print(f"{'='*50}")
    print(f"Equação: Óbitos = {modelo.coef_[0]:.2f} * Ano + {modelo.intercept_:.2f}")
    print(f"Coeficiente de determinação (R²): {r2:.4f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"Tendência: {'CRESCENTE' if modelo.coef_[0] > 0 else 'DECRESCENTE'}")
    
    # Gráfico melhorado
    plt.figure(figsize=(12, 6))
    plt.scatter(X, y, alpha=0.7, s=60, label="Dados observados")
    plt.plot(X, y_pred, color="red", linewidth=3, label="Linha de regressão")
    
    # Previsão para próximos anos (opcional)
    if len(df) > 3:
        anos_futuros = np.array([[df['ano'].max() + 1], [df['ano'].max() + 2]])
        pred_futuro = modelo.predict(anos_futuros)
        plt.scatter(anos_futuros, pred_futuro, color='green', s=100, 
                   marker='*', label='Previsão', zorder=5)
    
    plt.title(f"Regressão Linear - Óbitos por Ano\n(R² = {r2:.3f})", fontsize=14)
    plt.xlabel("Ano", fontsize=12)
    plt.ylabel("Óbitos", fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

# ===== 4. EXECUÇÃO PRINCIPAL =====
def main():
    arquivo = "3124.xlsx"
    
    print("🚀 Iniciando análise de dados de mortalidade...")
    
    # Ler dados
    tabelas = ler_dados_excel(arquivo)
    
    if not tabelas:
        print("❌ Nenhum dado válido encontrado!")
        return
    
    # Concatenar dados
    df_final = pd.concat(tabelas, ignore_index=True)
    
    print(f"\n✅ Base final criada com {len(df_final)} registros")
    print(f"📋 Colunas disponíveis: {list(df_final.columns)}")
    
    # Análises
    analise_exploratoria(df_final)
    analise_regressao(df_final)
    
    # Estatísticas descritivas
    print(f"\n{'='*50}")
    print("📊 ESTATÍSTICAS DESCRITIVAS")
    print(f"{'='*50}")
    
    colunas_existentes = [c for c in ["obitos", "populacao", "taxa"] if c in df_final.columns]
    estatisticas = df_final[colunas_existentes].describe().T
    estatisticas['cv'] = estatisticas['std'] / estatisticas['mean']  # Coeficiente de variação
    print(estatisticas.round(2))
    
    # Salvar dados processados
    df_final.to_excel('dados_processados.xlsx', index=False)
    print(f"\n💾 Dados processados salvos em 'dados_processados.xlsx'")

if __name__ == "__main__":
    main()

