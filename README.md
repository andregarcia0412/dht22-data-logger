# 🌡️ DHT22 Data Logger

Temperature and humidity monitoring system using **Arduino** and **DHT22**, sending data to **Python** and saving it in **CSV** format for later analysis using **Pandas**.
---
# ⚙️ Work In Progress...
## 📌 Features
- Real-time temperature and humidity readings
- Arduino ↔ Python communication via serial port
- Automatic saving of data to `.csv` file
- Data analysis and visualization with Pandas and Matplotlib

## ⚙️ Technologies Used
- **Hardware**
  - **Arduino Uno**
  - **DHT22 Sensor**
  - **4K7 Pull-up Resistor**
  - **4x Jumper Wires**
- **Software**
  - **Python**
  - **Python Libraries:** `pandas`, `matplotlib`, `seaborn`, `pyserial`, `customTkinter`, `datetime`, `time` 
  - **Arduino IDE** for microcontroller programming
  - **Arduino Libraries:** `Adafruit_Sensor.h`

## 🖼️ System Workflow
Arduino (DHT22) → Serial → Python → CSV → Pandas → Graphs

## 🚀 How to Use
### 1️⃣ Arduino
1. Open `dht22-config.ino` in the Arduino IDE.
2. Upload it to the board.
3. Connect the DHT22 according to the wiring diagram.

<img src="https://blog.eletrogate.com/wp-content/uploads/2019/01/Arduino-DHT11-DHT22_editado2-1024x566.jpg">

### 2️⃣ Python
1. Install the dependencies:
   ```bash
   pip install pandas matplotlib seaborn pyserial customtkinter
2. Run the script data_collect.py to collect temperature and humidity data.

3. Run the script data_analysis.py to generate graphs and statistics.
