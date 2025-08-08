import serial
import csv
import time
from datetime import datetime
import customtkinter as ctk

arduino_port = "COM4"
baud_rate = 9600
file_name = "data_science_temp_hum/arduino_data.csv"

reading = True
def stop_data_reading():
    global reading
    reading = False
    main.destroy()

ctk.set_appearance_mode('system')
main = ctk.CTk()
stop_button = ctk.CTkButton(main, command=stop_data_reading, text="Stop", fg_color = "red", hover_color="#C0392B")
stop_button.pack()

try:
    ser = serial.Serial(arduino_port, baud_rate)
    time.sleep(2)
    with open(file_name, "a", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        while reading:
            main.update()
            if ser.in_waiting > 0:
                line = ser.readline().decode("utf-8").strip()
                data = line.split(",")
                if len(data) == 2:
                    csv_writer.writerow([data[0], data[1], datetime.now().hour])
                    print(f"Written data: {data}")
except serial.SerialException as e:
    print(f"Error in serial port {e}")
except Exception as e:
    print(f"An error has ocurred {e}")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
