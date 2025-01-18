import base64
import io

import matplotlib.pyplot as plt


def plot_results(results):
    plt.figure(figsize=(12, 6))
    months = [r["month"] for r in results]
    net_profits = [r["net_profit"] for r in results]
    adjusted_sales = [r["adjusted_sales"] for r in results]

    plt.plot(months, net_profits, marker="o", label="Net Profit", color="green")
    plt.plot(months, adjusted_sales, marker="x", label="Adjusted Sales", color="blue")
    plt.title("Financial Simulation for 12 Months")
    plt.xlabel("Month")
    plt.ylabel("Values ($)")
    plt.axhline(0, color="red", linestyle="--", label="Break-even")
    plt.legend()
    plt.grid()
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)

    return base64.b64encode(img.getvalue()).decode()
