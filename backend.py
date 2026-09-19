import pandas as pd
import json
import sqlite3

try:
    df = pd.read_csv('amazon.csv')
except FileNotFoundError:
    print("Erro: o arquivo 'amazon.csv' não foi encontrado. Verifique se ele está na pasta do projeto.")
    exit()

# Tratar o caso de a base estar vazia
if df.empty:
    print("Erro: a base de dados está vazia.")

# Tratar valores nulos
df = df.dropna(subset=['rating_count'])

# Limpar e converter preços
df['discounted_price'] = df['discounted_price'].str.replace('₹', '').str.replace(',', '').astype(float)
df['actual_price'] = df['actual_price'].str.replace('₹', '').str.replace(',', '').astype(float)

# Limpar e converter desconto
df['discount_percentage'] = df['discount_percentage'].str.replace('%', '').astype(float)

# Remover linha inválida e converter rating
df = df[df['rating'] != '|']
df['rating'] = df['rating'].astype(float)

# Limpar e converter rating_count
df['rating_count'] = df['rating_count'].str.replace(',', '').astype(float)

# Extrair categoria principal
df['categoria_principal'] = df['category'].str.split('|').str[0]

# Criar (ou conectar) o banco SQLite
conexao = sqlite3.connect('banco.db')

# Salvar os dados tratados na tabela 'produtos'
df.to_sql('produtos', conexao, if_exists='replace', index=False)

# Testar: rodar uma consulta simples pra confirmar que funcionou
teste = pd.read_sql('SELECT product_name, rating FROM produtos LIMIT 5', conexao)
print("Teste do banco SQL:")
print(teste)

conexao.close()

# Montar o dicionário com todos os indicadores
indicadores = {
    "preco_medio_com_desconto": round(df['discounted_price'].mean(), 2),
    "desconto_medio_percentual": round(df['discount_percentage'].mean(), 2),
    "avaliacao_media": round(df['rating'].mean(), 2),
    "volume_total_avaliacoes": int(df['rating_count'].sum()),
    "distribuicao_por_categoria": df['categoria_principal'].value_counts().to_dict()
}

# Salvar em um arquivo JSON
with open('dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(indicadores, arquivo, ensure_ascii=False, indent=4)

print("Arquivo dados.json gerado com sucesso!")
print(indicadores)