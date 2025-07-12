import yfinance as yf
import matplotlib.pyplot as plt

def plot_line_chart(ticker):
    data = yf.download(ticker, period="1y")

    fig = plt.figure(figsize=(5.77, 4), dpi=200) 
    fig.set_facecolor("#dddddd")
    ax = fig.add_subplot(111)
    ax.plot(data.index, data['Close'], color="#0000ff", label='Close Price') 
    ax.set_title(f"{ticker} Close Price")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.set_facecolor("#FFFFFF")
    ax.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    ticker = input("Enter ticker symbol: ").upper()
    plot_line_chart(ticker)
