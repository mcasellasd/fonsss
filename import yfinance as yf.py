import yfinance as yf

# Substitueix 'ticker' pel ticker associat al teu ISIN
ticker = "F00000VW7L"  # Exemple de ticker de fons
fund = yf.Ticker(ticker)

# Obtenim informació del fons
fund_info = fund.info
print(fund_info)

# Exemple d'obtenció de dades històriques
hist = fund.history(period="1mo")
print(hist)