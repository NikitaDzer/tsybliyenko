import matplotlib.pyplot as plt
import numpy as np


MAX_VOLTAGE = 3.3
DAC_BITS    = 8
DAC_LEVELS  = 2 ** DAC_BITS

DATA_FILE_PATH     = "data.txt"
SETTINGS_FILE_PATH = "settings.txt"
FIGURE_FILE_PATH   = "figure.svg"

DISCRET_POSITION  = 0
EXP_TIME_POSITION = 2

FIGURE_SIZE = (20, 15)



def read_data(file_path):
    with open(file_path, "r") as file:
        data_str = file.read().split()
        data = np.array(list(map(float, data_str)))

    return data


def convert_to_voltage(data):
     for i in range(len(data)):
        data[i] = data[i] / DAC_LEVELS * MAX_VOLTAGE

def plot_data():
    data     = read_data(DATA_FILE_PATH)
    settings = read_data(SETTINGS_FILE_PATH)

    convert_to_voltage(data)

    discret  = settings[DISCRET_POSITION]
    exp_time = settings[EXP_TIME_POSITION]

    values_y = data
    values_x = np.arange(start = discret, stop = exp_time, step = discret)

    charging_time    = get_charging_time(data, discret)
    discharging_time = get_discharging_time(exp_time, charging_time)

    figure, axes = plt.subplots(figsize = FIGURE_SIZE, dpi = 150)

    axes.minorticks_on()
    plt.plot(values_x, values_y, color = "black", label = "V(t)", marker = "o", markevery = 300, markersize = 10, linewidth = 0.5)

    plt.text(0.8 * values_x.max(), 0.8 * values_y.max(),
             f"Experiment time is:  {exp_time:.2f} s\n"
             f"Charging time is:    {charging_time:.2f} s\n"
             f"Discharging time is: {discharging_time:.2f} s\n")

    plt.title("Capacitor's charging and discharging in RC-circut")
    plt.xlabel("Time, s")
    plt.ylabel("Voltage, V")

    plt.xlim([0, exp_time])
    plt.ylim([0, max(data) + 0.1])

    plt.grid(which = "major", linestyle = "-",  linewidth = 1)
    plt.grid(which = "minor", linestyle = "--", linewidth = 0.5)
    plt.legend()

    plt.savefig(FIGURE_FILE_PATH)

    plt.show()


def get_charging_time(data, discret):
    return data.argmax() * discret 


def get_discharging_time(exp_time, charging_time):
    return exp_time - charging_time


plot_data()