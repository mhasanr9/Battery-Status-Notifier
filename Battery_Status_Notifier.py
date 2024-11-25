import psutil  # fetch system and hardware information
import time    # implement delays
from plyer import notification  # show desktop notifications

#Function that hold all the necessary codes
def check_battery():

    battery = psutil.sensors_battery() #this is for getting battery status

    if battery:
        percent = battery.percent
        plugged = battery.power_plugged

        # Check the conditions
        if percent > 90 and plugged:
            notification.notify(
                title="⚠️ Battery Charged Above Threshold ⚠️",
                message=f"Battery is at {percent}%. Consider unplugging the charger.",
                timeout=10
            )
        elif percent < 90 and not plugged:
            notification.notify(
                title="⚠️ Battery Charged Below Threshold ⚠️",
                message=f"Battery is at {percent}%. Consider plugging the charger.",
                timeout=10
            )
    else:
        print("Battery information could not be retrieved.")

if __name__ == "__main__":
    while True:
        check_battery()  # Call the function to check battery status
        time.sleep(5*60)  # Wait for defined seconds before the next check
