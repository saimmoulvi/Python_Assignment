#importing psutil to retreive system information / CPU usage
import psutil
import time

#Defining the CPU usage threshold in percentage
THRESHOLD = 80.0 

#implementing function monitor_cpu_usage to monitor CPU usage threshold
def monitor_cpu_usage():
    print("Monitoring CPU Usage....")

    try:
        while True:
            #Getting the current CPU Usage
            cpu_usage = psutil.cpu_percent(interval=1)

            #Checking if the CPU usage exceeds the threshold
            if cpu_usage > THRESHOLD:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

            #Sleep for a short while before checking again
            time.sleep(1)

    except KeyboardInterrupt:
        print("CPU monitoring stopped by the user.")
    except Exception as e:
        print(f"An error ocurred: {e}")

if __name__ == "__main__":
    monitor_cpu_usage()                        