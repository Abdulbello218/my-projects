import pandas as pd
import matplotlib.pyplot as plt

def mass_balance(streams_data):
    df = pd.DataFrame(streams_data)
    total_flow = df["flow_rate"].sum()
    mass_solute = df["flow_rate"] * df["concentration"]
    outlet_concentration = mass_solute.sum() / total_flow
    weighted_temp = df["flow_rate"] * df["temperature"]
    mixed_temperature = weighted_temp.sum() / total_flow
    
    print(df)
    print(f"\nTotal flow rate: {total_flow} kg/hr")
    print(f"Outlet concentration: {outlet_concentration:.3f} kg/kg")
    print(f"Mixed temperature: {mixed_temperature:.1f} °C")
    return df

def plot_streams(df):
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.bar(df["stream"], df["flow_rate"], color="steelblue")
    plt.title("Flow Rates")
    plt.ylabel("kg/hr")
    plt.subplot(1, 2, 2)
    plt.bar(df["stream"], df["concentration"], color="coral")
    plt.title("Concentrations")
    plt.ylabel("kg/kg")
    plt.tight_layout()
    plt.show()

def main():
    streams = {
        "stream": ["Feed 1", "Feed 2", "Feed 3", "Feed 4"],
        "flow_rate": [100, 150, 80, 120],
        "temperature": [25, 60, 40, 35],
        "concentration": [0.8, 0.5, 0.3, 0.6]
    }
    df = mass_balance(streams)
    plot_streams(df)

main()