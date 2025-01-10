# Bitcoin Price Viewer

Visualizador em tempo real do preço do Bitcoin usando dados da API Binance.

## Features
- Gráfico candlestick atualizado em tempo real
- Alternância entre modo histórico e tempo real
- Exibição de preço atual e variação 24h
- Dados diretos da Binance Futures API
- Customização de intervalos

## Requisitos
- Python 3.x
- Conexão internet estável
- Bibliotecas listadas em requirements.txt

## Instalação
1. Clone o repositório:
  - git clone https://github.com/seu-usuario/bitcoin-price-viewer
  - cd bitcoin-price-viewer

2. Instale dependências:
  - pip install -r requirements.txt

3. Execute:
     - pip install -r requirements.txt
  
Como Usar
Interface

Gráfico principal: Exibe candlesticks
Botão "Toggle Mode":

Alterna entre tempo real e histórico
Tempo real: Atualização a cada minuto
Histórico: Exibe últimas 50 velas diárias



Dados Exibidos

Candlesticks: Preços high, low, open, close
Preço atual em USD
Variação percentual 24h
Volume de negociação

Modos

Tempo Real

Atualização automática cada 1 min
Exibe últimas 50 velas de 1 min
Preço atual e variação no topo


Histórico

Dados diários
Últimas 50 velas
Sem atualização automática



Limitações

Requer conexão internet estável
Dados limitados à API Binance
Máximo 50 velas por vez

Licença
MIT


