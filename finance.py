import yfinance as yf

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    print(f"Stock: {info['shortName']} ({ticker})")
    print(f"Current Price: ${info['currentPrice']:.2f}")
    print(f"Market Cap: ${info['marketCap']:,}")
    print(f"Summary: {info['longBusinessSummary']}")

def main():
    while True:
        ticker = input("Enter a stock ticker (or 'q' to quit): ").upper()
        if ticker == 'Q':
            break
        try:
            get_stock_info(ticker)
        except Exception as e:
            print(f"An error occured: {e}")
        print()

main()