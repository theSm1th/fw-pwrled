import time
import os

# Variables
# The path to your battery information. This is a default that works for my FW, unsure if it is different for other FWs.
batt_path = "/sys/class/power_supply/BAT1/"

# The battery percentage to switch to a red LED when below or equal to.
critical_percentage = 20

# The interval that this script will check for battery percentage changes. 15 is a sane default. A lower interval
# will update more often but will use more processing power in the background, as it checks more often.
check_interval = 15

# Enables the power led turning green while a charger is connected. If false, only the red light for critical battery
# will be checked and executed.
enable_green_during_charge = True

# Main loop
while True:
    # Read battery status (BAT# /status) - this tells us if the battery is charging or discharging
    with open(batt_path + "status") as status_file:
        battery_status = status_file.read().strip()
    if battery_status == "Charging" and enable_green_during_charge:
        os.system("sudo ectool led power green")
    else:
        # Get battery percentage from the appropriate BAT# file (/capacity) - placed here in the else statement
        # (instead of using an elif) to avoid unnecessary reads from disk
        with open(batt_path + "capacity", "r") as capacity_file:
            battery_percentage = int(capacity_file.read())

        if battery_percentage <= critical_percentage:
            # Set the power led to red
            os.system("sudo ectool led power red")
        else:
            # In this case, the battery is neither in critical percentage nor charging - hand over control of the
            # light to EC.
            os.system("sudo ectool led power auto")
    time.sleep(check_interval)
