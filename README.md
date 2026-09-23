# Dashboard Web de Vendas e Atendimento

Painel que mostra indicadores de vendas e atendimento, usando banco SQL, Python e uma página web.

Projeto do Tech Girls Challenge — Equipe Manhã.

## Equipe

- Amanda — Frontend https://www.linkedin.com/in/amanda-carvalho-949930196/?isSelfProfile=true
- Allana da Cruz — Backend, dados e SQL

## Stack

SQLite, Python (pandas), HTML, CSS

## Base de dados

[Amazon Sales Dataset](https://www.kaggle.com/code/mehakiftikhar/amazon-sales-dataset-eda) (Kaggle) — dados de produtos, preços, descontos e avaliações de clientes.

Baixe o arquivo `amazon.csv` do Kaggle e coloque na raiz do projeto (mesma pasta do `backend.py`) antes de rodar.

## Como rodar

```bash
# 1. Clonar o repositório
git clone <link-do-repositorio>
cd <nome-da-pasta>

# 2. Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# 3. Instalar as dependências
pip install pandas

# 4. Colocar o arquivo amazon.csv na pasta do projeto (baixado do Kaggle)

# 5. Rodar o script (gera o banco.db e o dados.json)
python backend.py

# 6. Subir um servidor local e abrir o painel
python -m http.server
# depois acessar http://localhost:8000 no navegador
```

**O que o `backend.py` faz:** lê o `amazon.csv`, trata valores nulos/inválidos, converte colunas de texto (preço e desconto) para número, salva os dados tratados num banco SQLite (`banco.db`, tabela `produtos`) e calcula os 5 indicadores, gerando o arquivo `dados.json` para o frontend consumir.
 
**Frontend**

Foi desenvolvido um dashboard web utilizando HTML e CSS, com o objetivo de apresentar de forma organizada e visual os principais indicadores dos dados de vendas e avaliações dos produtos.

A interface foi estruturada em diferentes seções:

*Cabeçalho*, com o título e uma breve descrição do dashboard.
*Visão geral*, apresentando a finalidade dos indicadores.
*Cards de indicadores*, destinados a apresentar:
*Preço médio* com desconto;
*Percentual médio* de desconto;
*Avaliação média* dos clientes;
*Volume total* de avaliações.
*Distribuição por categoria*, utilizando barras de progresso para facilitar a visualização da quantidade de produtos por categoria principal.
*Resumo dos indicadores*, reunindo os principais resultados da análise.
*Tabela de produtos*, preparada para apresentar informações como produto, categoria, preço com desconto, percentual de desconto, avaliação e quantidade de avaliações.
*Layout responsivo*, permitindo que a interface se adapte a diferentes tamanhos de tela, como computadores, tablets e celulares.

O **CSS** foi desenvolvido com foco em uma interface limpa e organizada, utilizando cards, painéis, tabela, espaçamentos, bordas, efeitos de interação e responsividade para melhorar a visualização e a experiência do usuário.

A estrutura do frontend também foi preparada para receber posteriormente os dados processados pelo Python/pandas, permitindo que os valores apresentados no dashboard sejam alimentados pela base amazon.csv.

## Indicadores

1. **Preço médio com desconto** — média do valor final pago pelo cliente (coluna `discounted_price`).
2. **Percentual médio de desconto** — média do desconto aplicado em relação ao preço original (coluna `discount_percentage`).
3. **Avaliação média** — nota média de 1 a 5 dada pelos clientes (coluna `rating`).
4. **Volume de avaliações** — soma do total de avaliações recebidas, indicando popularidade (coluna `rating_count`).
5. **Distribuição por categoria principal** — contagem de produtos por categoria, usando apenas o primeiro nível da coluna `category` (ela vem com o caminho completo, tipo "Computers&Accessories|Accessories&Peripherals|Cables", então é tratada para pegar só a parte antes do primeiro "|").

## Status

- [x] Base de dados definida (Amazon Sales Dataset)
- [x] Indicadores definidos
- [x] Banco SQL pronto (SQLite, tabela `produtos`)
- [x] Script Python pronto (`backend.py` gera `banco.db` e `dados.json`)
- [x] Tratamento de erros testado (arquivo ausente)
- [ ] Página web pronta
- [ ] Gráfico pronto
