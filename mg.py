import yfinance as yf
import matplotlib.pyplot as plt
import math

def plot_mini_charts(tickers):
    num_tickers = len(tickers)
    cols = 3  # You can adjust this
    rows = math.ceil(num_tickers / cols)

    fig, axes = plt.subplots(rows, cols, figsize=(6 * cols, 4 * rows), dpi=100)
    fig.patch.set_facecolor("#dddddd")
    axes = axes.flatten()

    for i, ticker in enumerate(tickers):
        data = yf.download(ticker, period="1y")
        ax = axes[i]
        ax.plot(data.index, data['Close'], color="#0000ff")
        ax.set_facecolor("#ffffff")

        # Small title and axis labels
        ax.set_title(ticker, fontsize=10)

        # Smaller ticks
        ax.tick_params(axis='both', which='major', labelsize=6)

    # Remove extra subplots if needed
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    input_str = input("Enter ticker symbols (comma-separated): ")
    tickers = [t.strip().upper() for t in input_str.split(",") if t.strip()]
    if tickers:
        plot_mini_charts(tickers)
