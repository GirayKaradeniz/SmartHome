# SmartHome

The Smart Home Load Management System is a Python-based application designed to optimize energy consumption in smart homes by implementing load shifting strategies. This project leverages the power of pandas for data manipulation and matplotlib for visualizing load graphs. Users can analyze their energy usage patterns throughout the day, apply load shifting techniques to reduce peak energy consumption, and calculate associated costs based on different pricing schemes.

## Features

- **Load Graph Generation**: Create visual representations of energy loads over time.
- **Load Shifting**: Shift energy loads from peak periods to off-peak periods based on priority levels.
- **Cost Calculation**: Calculate energy costs based on morning, peak, and night rates.
- **Data Management**: Read from and write to Excel files for easy data management.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-home-load-management.git
   cd smart-home-load-management
2. Install the required packages:
   ```bash
   pip install pandas matplotlib openpyxl
## Usage

1. Update the parameters in the script, such as morning, peak, and night rates as well as the threshold for load shifting.
   
2. Run the main script:
  ```bash
  python main.py
