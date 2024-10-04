import pandas as pd
import matplotlib.pyplot as plt
from Functions import CreatingLoadGraph as Clg
from Functions import LoadShifting as Ls
from Functions import Pricing as Pr

morning = 3.15
peak = 4.62
night = 1.97
Threshold = 4

Data = pd.read_excel("SmartHomeData.xlsx")

# Create load graph and get load and time
result = Clg.creating_load_graph(Data)

# Check if result is None
if result is not None:
    load, timeOfTheDay = result  # Unpack the load and time

shifting_data = Data.copy()
shifting = Ls.load_shifting(shifting_data, Threshold)

shftdData = pd.read_excel("Temp.xlsx")

# Create load graph for shifted data and get load and time
shifted_result = Clg.creating_load_graph(shftdData)

# Check if shifted_result is None
if shifted_result is not None:
    shifted_load, shifted_timeOfTheDay = shifted_result  # Unpack the load and time

price = Pr.calculate_price(Data, morning, peak, night)
shiftedPrice = Pr.calculate_price(shftdData, morning, peak, night)

# Plot both graphs in a single figure
plt.figure(figsize=(12, 6))

# Original load graph
plt.subplot(1, 2, 1)
plt.plot(timeOfTheDay, load, label='Orijinal Yük Grafiği')
plt.xticks(rotation=45)
plt.title('Orijinal Yük Grafiği')
plt.xlabel('Zaman')
plt.ylabel('Yük (kW)')
plt.legend()

# Shifted load graph
plt.subplot(1, 2, 2)
plt.plot(shifted_timeOfTheDay, shifted_load, label='Kaydırılmış Yük Grafiği', color='orange')
plt.xticks(rotation=45)
plt.title('Kaydırılmış Yük Grafiği')
plt.xlabel('Zaman')
plt.ylabel('Yük (kW)')
plt.legend()

# Adjust layout and show
plt.tight_layout()
plt.show()




