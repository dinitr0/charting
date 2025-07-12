import yfinance as yf
import matplotlib.pyplot as plt

def plot_percent_change_chart(tickers):
    data = yf.download(tickers, period="ytd")['Close']

    # Normalize to 0% at the start
    norm_data = (data / data.iloc[0] - 1) * 100  # percent change

    fig = plt.figure(figsize=(6, 4), dpi=200)
    fig.set_facecolor("#dddddd")
    ax = fig.add_subplot(111)

    for ticker in norm_data.columns:
        ax.plot(norm_data.index, norm_data[ticker], label=ticker)

    ax.set_title("ytd Percent Change")
    ax.set_xlabel("Date")
    ax.set_ylabel("Percent Change (%)")
    ax.set_facecolor("#ffffff")
    ax.legend()
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    ticker_input = input("Enter ticker symbols (comma-separated): ").upper()
    tickers = [t.strip() for t in ticker_input.split(',')]
    plot_percent_change_chart(tickers)
