import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def formato_data(df, colunas):
    'Função para ajuste para o tipo de datetime das colunas de data'
    for col in colunas:
        df[col] = pd.to_datetime(df[col].astype(str).str[:10], format='%Y-%m-%d', errors='coerce')
    return df

def calcular_media_lat_lng(df, zip_col, lat_col, lng_col, lat_media, lng_media):
    'Função para calcular a média da latitude e longitude'
    df[lat_media] = df.groupby(zip_col)[lat_col].transform('mean')
    df[lng_media] = df.groupby(zip_col)[lng_col].transform('mean')
    return df

def estatisticas(df):
    'função para calcular as estatísticas de um conjunto de dados'
    estatisticas = df.describe().T.reset_index()
    estatisticas.columns = ['feature','quantidade','média','desvio-padrão', 
                            'minimo','1Q','2Q','3Q','máximo']
    estatisticas['mediana'] = estatisticas['2Q']
    estatisticas['IQR'] = estatisticas['3Q'] - estatisticas['1Q']
    return estatisticas

def histogramas(df, colunas, titulos, xlabels):
    """
    Função para plotar histogramas personalizados.
    
    Parâmetros:
        df (DataFrame): DataFrame contendo os dados.
        colunas (list): Lista com os nomes das colunas a serem plotadas.
        titulos (list): Lista com os títulos dos gráficos.
        xlabels (list): Lista com os nomes dos eixos X.
    """
    
    if not (len(colunas) == len(titulos) == len(xlabels)):
        raise ValueError("As listas 'colunas', 'titulos' e 'xlabels' devem ter o mesmo tamanho.")

    plt.figure(figsize=(12, 12))
    plt.suptitle('Histogramas', fontsize=18, fontweight='bold')

    for i, col in enumerate(colunas):
        plt.subplot(2, 2, i+1)  # Ajusta dinamicamente a posição dos gráficos
        plt.hist(df[col], bins=30, color='blue', edgecolor='black')
        plt.xlabel(xlabels[i])
        plt.ylabel('Frequência')
        plt.title(titulos[i])

    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.show()

def dispersao(df, colunas, titulos, xlabels, ylabels, colors):
    """
    Função para plotar gráficos de dispersão personalizados.
    
    Parâmetros:
        df (DataFrame): DataFrame contendo os dados.
        colunas (list): Lista de tuplas com as colunas a serem usadas no eixo X e Y.
        titulos (list): Lista com os títulos dos gráficos.
        xlabels (list): Lista com os nomes dos eixos X.
        ylabels (list): Lista com os nomes dos eixos Y.
        colors (list): Lista com as cores dos pontos em cada gráfico.
    """
    
    if not (len(colunas) == len(titulos) == len(xlabels) == len(ylabels) == len(colors)):
        raise ValueError("As listas 'colunas', 'titulos', 'xlabels', 'ylabels' e 'colors' devem ter o mesmo tamanho.")
    
    plt.figure(figsize=(12, 12))
    plt.suptitle('Dispersão', fontsize=18, fontweight='bold')

    for i, (x_col, y_col) in enumerate(colunas):
        plt.subplot(len(colunas), 1, i+1)
        sns.scatterplot(df, x=x_col, y=y_col, color=colors[i])
        plt.xlabel(xlabels[i])
        plt.ylabel(ylabels[i])
        plt.title(titulos[i], fontweight='bold')

    plt.subplots_adjust(hspace=0.5)
    plt.show()

def box_plot(df, colunas, titulos, ylabels, colors):
    """
    Função para plotar gráficos de box-plot personalizados.
    
    Parâmetros:
        df (DataFrame): DataFrame contendo os dados.
        colunas (list): Lista com os nomes das colunas a serem plotadas.
        titulos (list): Lista com os títulos dos gráficos.
        ylabels (list): Lista com os nomes dos eixos Y.
        colors (list): Lista com as cores dos gráficos.
    """
    
    if not (len(colunas) == len(titulos) == len(ylabels) == len(colors)):
        raise ValueError("As listas 'colunas', 'titulos', 'ylabels' e 'colors' devem ter o mesmo tamanho.")
    
    plt.figure(figsize=(12, 12))
    plt.suptitle('Box-plot', fontsize=18, fontweight='bold')

    for i, col in enumerate(colunas):
        plt.subplot(2, 2, i+1)  # Ajusta dinamicamente a posição dos gráficos
        sns.boxplot(y=df[col], color=colors[i])
        plt.ylabel(ylabels[i])
        plt.title(titulos[i], fontweight='bold')

    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    plt.show()

def z_score_col(df, col, z_score_col ):
    df[z_score_col] = (df[col] - df[col].mean()) / df[col].std()
    return df