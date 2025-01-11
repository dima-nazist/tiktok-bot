from selenium import webdriver
from os import system, name
import chromedriver_binary
from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading
import chromedriver_autoinstaller

# Check if the current version of chromedriver exists and, if it doesn't exist, download it automatically
chromedriver_autoinstaller.install()

def clear_terminal():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear_terminal()
system('title PROGRAM_NAME')

print(pyfiglet.figlet_format("PROGRAM_NAME", font="slant"))
print("1. Option 1.\n2. Option 2.\n3. Option 3.\n4. Option 4.\n5. Credits.\n")

mode = int(input("Mode: "))

if mode == 1 or mode == 2 or mode == 3 or mode == 4:
    url = input("URL: ")

    start = time()
    time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))

    # Chrome options to run the browser with some configurations
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Ensure the chromedriver path is correctly set up
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1024, 650)

    metric1 = 0
    metric2 = 0
    metric3 = 0

def beautify(arg):
    return format(arg, ',d').replace(',', '.')

def update_title1():  # Update the title IF option 1 was picked.
    global metric1
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title PROGRAM_NAME ^| Metric 1: {beautify(metric1)} ^| Elapsed Time: {time_elapsed}')
        sleep(1)

def update_title2():  # Update the title IF option 2 was picked.
    global metric2
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title PROGRAM_NAME ^| Metric 2: {beautify(metric2)} ^| Elapsed Time: {time_elapsed}')
        sleep(1)

def update_title3():  # Update the title IF option 3 was picked.
    global metric3
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title PROGRAM_NAME ^| Metric 3: {beautify(metric3)} ^| Elapsed Time: {time_elapsed}')
        sleep(1)

# Threads to update title based on selected option
if mode == 1:
    threading.Thread(target=update_title1, daemon=True).start()
elif mode == 2:
    threading.Thread(target=update_title2, daemon=True).start()
elif mode == 3:
    threading.Thread(target=update_title3, daemon=True).start()

# Simulate the program doing work by updating metrics
# You can add your logic to increment these metrics based on the tasks performed
try:
    while True:
        if mode == 1:
            metric1 += 1
        elif mode == 2:
            metric2 += 1
        elif mode == 3:
            metric3 += 1
        
        # Simulate doing work and updating the metrics
        sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
    driver.quit()
