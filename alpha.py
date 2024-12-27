from alpha_vantage.timeseries import TimeSeries

# Substitueix 'your_api_key' per la teva clau API d'Alpha Vantage
api_key = 'M21KY5DESE6LYBD6'
ts = TimeSeries(key=api_key, output_format='pandas')

# Obtenim dades de la sèrie temporal d'un actiu
symbol = 'MSFT'  # Substitueix per un símbol que t'interessi
data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')

# Mostrem les dades
print(data.head())