import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mplfinance as mpf

# Variáveis globais
current_price = 0.0
percent_change_24h = 0.0
update_interval = 1000  # Intervalo padrão de atualização (1 minuto)
real_time_update = True  # Modo tempo real ativado por padrão

def get_binance_data(interval):
   url = "https://api.binance.com/api/v3/klines"
   params = {
       'symbol': 'BTCUSDT',   
       'interval': interval,  
       'limit': 50         
   }
   response = requests.get(url, params=params)
   data = response.json()
   df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 
                                  'close_time', 'quote_asset_volume', 'number_of_trades', 
                                  'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
   df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
   df.set_index('timestamp', inplace=True)
   df = df.astype(float)
   return df

def update_current_price_and_change(i):
   global current_price, percent_change_24h
   url_price = "https://api.binance.com/api/v3/ticker/price"
   params_price = {'symbol': 'BTCUSDT'}
   response_price = requests.get(url_price, params=params_price)
   data_price = response_price.json()
   current_price = float(data_price['price'])

   url_24h = "https://api.binance.com/api/v3/ticker/24hr"
   params_24h = {'symbol': 'BTCUSDT'}
   response_24h = requests.get(url_24h, params=params_24h)
   data_24h = response_24h.json()
   percent_change_24h = float(data_24h['priceChangePercent'])

def update_candlestick(i):
   global update_interval
   if real_time_update:
       interval = '1m'
       update_current_price_and_change(0)
       df = get_binance_data(interval)
       ax.clear()
       mpf.plot(df, type='candle', style='charles', ax=ax)
       ax.text(df.index[-1], df['close'].iloc[-1], 
               f'Current Price: ${current_price:.2f} ({percent_change_24h:.2f}%)', 
               fontsize=10, ha='right', va='bottom', color='white')
       ax.annotate(f'Current Price: ${current_price:.2f} ({percent_change_24h:.2f}%)', 
                  xy=(0.5, 0.95), xycoords='axes fraction', 
                  fontsize=10, ha='center', va='top', color='white')
   else:
       ax.clear()
       df = get_binance_data('1d')
       mpf.plot(df, type='candle', style='charles', ax=ax)

def toggle_update_mode(event):
   global real_time_update, update_interval
   real_time_update = not real_time_update
   if real_time_update:
       update_interval = 1000
       candlestick_ani.event_source.interval = update_interval
   else:
       update_interval = None
       candlestick_ani.event_source.stop()
       update_candlestick(0)

# Configuração do gráfico
plt.style.use('dark_background')
fig, ax = plt.subplots()

# Animação do gráfico
candlestick_ani = FuncAnimation(fig, update_candlestick, interval=update_interval, 
                              cache_frame_data=False)

# Botão toggle
ax_button = plt.axes([0.7, 0.025, 0.1, 0.04])
button = plt.Button(ax_button, 'Toggle Mode')
button.on_clicked(toggle_update_mode)

plt.show()
