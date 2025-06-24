#Alram Clock 

import time
import datetime
import winsound  # For Windows sound alert (use other methods for Linux/Mac)

def set_alarm(alarm_time):
    """Waits until the alarm time is reached and then plays a sound."""
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("⏰ Wake up! Alarm ringing...")

            # Play a beep sound (Windows)
            for _ in range(5):  
                winsound.Beep(1000, 500)  # Frequency 1000Hz, Duration 500ms
            
            break  # Stop checking after the alarm rings
        time.sleep(10)  # Check time every 10 seconds to save CPU usage

# Get user input for alarm time in HH:MM format
alarm_time = input("Enter alarm time (HH:MM in 24-hour format): ")
set_alarm(alarm_time)
