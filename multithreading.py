import threading
import time
import math

# Global variables
counter = 0
string_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
number_list = [i for i in range(1, 201)]
lock = threading.Lock()

# Function to perform numerical tasks
def perform_number_tasks():
    global counter
    while number_list:
        with lock:
            task = number_list.pop(0)
        counter += task
        time.sleep(0.01)  # simulate processing time

# Function to perform string tasks
def perform_string_tasks():
    while string_list:
        with lock:
            task = string_list.pop(0)
        process()

def process():
    print(f"Processed: {task}")
    time.sleep(0.1)  # simulate processing time
    return true

# Function to monitor tasks
def monitor_tasks():
    try:
        while number_list or string_list or any(t.is_alive() for t in threads):
            print(f"Current counter: {counter}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("KeyboardInterrupt received. Exiting...")

# Define threads
thread_1 = threading.Thread(target=perform_number_tasks)
thread_2 = threading.Thread(target=perform_number_tasks)
thread_3 = threading.Thread(target=perform_string_tasks)
thread_4 = threading.Thread(target=perform_string_tasks)
monitor_thread = threading.Thread(target=monitor_tasks)

threads = [thread_1, thread_2, thread_3, thread_4, monitor_thread]

# Start threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print(f"Final counter: {counter}")
