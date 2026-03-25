import time
import datetime
import os
import shlex
import subprocess
import threading

# Global event to signal the audio playback thread to stop.
stop_alarm_event = threading.Event()

# Path to the alarm sound file. Adjust this path to your local file.
alarm_file = "/Users/tahirsallie/Downloads/А.Х.  Prayer (Live)    Reinhardt Buhr.mp3"


def play_alarm_loop():
    # Verify sound file exists first before attempting playback.
    if not os.path.exists(alarm_file):
        print("Alarm file not found:", alarm_file)
        return

    # Loop playback until the stop event is set by the user.
    while not stop_alarm_event.is_set():
        proc = subprocess.Popen(["afplay", alarm_file])

        # Check the process status regularly so we can interrupt quickly.
        while proc.poll() is None and not stop_alarm_event.is_set():
            time.sleep(0.1)

        # If user requested stop while sound is playing, terminate the process.
        if stop_alarm_event.is_set() and proc.poll() is None:
            proc.terminate()
            proc.wait()
            break


def snooze_or_stop():
    # Prompt user while alarm is playing and decide whether to stop or snooze.
    # 'S' stops playback and exits alarm mode.
    # 'Z' snoozes for a short duration and returns control to scheduler.

    while True:
        choice = input("Enter 'S' to stop, 'Z' to snooze 5 minutes: ").strip().lower()
        if choice == 's':
            stop_alarm_event.set()
            return 'Stop'
        if choice == 'z':
            stop_alarm_event.set()
            return 'Snooze'
        print("Invalid option. Type 's' or 'z'.")


def main():
    while True:
        alarm_input = input("Set an alarm (HH:MM) or type 'exit' to quit:")
        if alarm_input.lower() == 'exit':
            print("Exiting alarm clock.")
            break

        try:
            alarm_time = datetime.datetime.strptime(alarm_input, "%H:%M").time()
            print(f"Alarm set for {alarm_time}.")
            while True:
                now = datetime.datetime.now().time()
                if now >= alarm_time:
                    print("Alarm ringing!")

                    # Reset event and start the sound thread for ringing.
                    stop_alarm_event.clear()
                    alarm_thread = threading.Thread(target=play_alarm_loop, daemon=True)
                    alarm_thread.start()

                    # Wait for user action to stop or snooze.
                    action = snooze_or_stop()
                    alarm_thread.join(timeout=5)

                    if action == 'Stop':
                        print("Alarm stopped.")
                        break

                    if action == 'Snooze':
                        snooze_minutes = 5
                        # Calculate new alarm time by adding snooze duration to now.
                        new_time = (datetime.datetime.combine(datetime.date.today(), now) + datetime.timedelta(minutes=snooze_minutes)).time()
                        print(f"Snoozed for {snooze_minutes} minutes. New alarm at {new_time}.")
                        alarm_time = new_time
                        continue

                # Poll every 30 seconds while waiting for the alarm.
                time.sleep(30)  # Check every 30 seconds
        except ValueError:
            print("Invalid time format. Please enter time as HH:MM.")


if __name__ == "__main__":
    main()
