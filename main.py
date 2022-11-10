import time
import os

batt_path = "/sys/class/power_supply/BAT1/"
critical_percentage = 15
check_interval = 30

while True:
    with open(batt_path + "capacity", "r") as capacity_file:
        battery_percentage = int(capacity_file.read())
    if battery_percentage <= critical_percentage:
        os.system("sudo ectool led power red")
    time.sleep(check_interval)