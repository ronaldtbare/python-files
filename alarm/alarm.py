from playsound3 import playsound
import time
import os

# playsound("alarm-clock.mp3")



def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60  # integer divide
        seconds_left = time_left % 60  # gives remainder for secs
        os.system('clear')
        print(f"Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}") #02d means make format 2 digits pad with 0

    print("Time's up!!!")
    
    print()
    print("Press CTRL + z to turn off.")
    # playsound("railroadcross.wav")
    playsound("alarm-clock.mp3")
    

minutes = int(input("How many minutes for timer: "))
seconds = int(input("How many minutes for timer: "))

total_seconds = minutes * 60 + seconds


alarm(total_seconds)


