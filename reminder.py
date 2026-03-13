import schedule
import time
from plyer import notification

def send_reminder(medicine):
    
    notification.notify(
        title="Medicine Reminder",
        message=f"Time to take your medicine: {medicine}",
        timeout=10
    )

# Example medicine reminder times
schedule.every().day.at("08:00").do(send_reminder, medicine="Paracetamol")
schedule.every().day.at("13:00").do(send_reminder, medicine="Vitamin C")
schedule.every().day.at("20:00").do(send_reminder, medicine="Insulin")

print("Medicine Reminder System Started...")

while True:
    schedule.run_pending()
    time.sleep(30)