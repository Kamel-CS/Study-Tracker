import time
import csv
from datetime import datetime
import math
import os

# List of your subjects
SUBJECTS = ["Project", "ICN", "IIS", "LT", "HT", "IDB", "OOP2"]

# Create directories if they don't exist
os.makedirs("data/logs", exist_ok=True)


def log_study():
    print("Welcome to Study Logger! Let's log your session.")

    while True:
        # Get subject name
        print("Available subjects:", ", ".join(SUBJECTS))
        subject = input("Enter the subject name (or 'q' to quit): ").strip()
        if subject.lower() == 'q':
            break
        if subject not in SUBJECTS:
            print("Invalid subject! Please choose from the list.")
            continue

        # Get specific task/goal
        task = input("Task: ").strip()

        # Start the session
        print(f"Studying {subject}: {task}. Press Enter to start the session.")
        input()
        start_time = time.time()
        last_pause_time = start_time
        total_paused_time = 0
        is_paused = False

        print("Session started. Press Enter to pause/resume or 'q' to finish.")

        while True:
            user_input = input()
            if user_input.lower() == 'q':
                break

            if is_paused:
                # Resume the session
                total_paused_time += time.time() - last_pause_time
                is_paused = False
                print("Session resumed. Press Enter to pause or 'q' to finish.")
            else:
                # Pause the session
                last_pause_time = time.time()
                is_paused = True
                print("Session paused. Press Enter to resume or 'q' to finish.")

        # Calculate total duration
        end_time = time.time()
        total_duration = end_time - start_time - total_paused_time
        duration_minutes = math.ceil(total_duration / 60)  # Round up to nearest minute

        # Get productivity score
        while True:
            try:
                productivity = int(input("Rate your productivity (1-10): "))
                if 1 <= productivity <= 10:
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Get notes
        notes = input("Notes about the session (optional): ").strip()

        # Log the session
        date = datetime.now().strftime('%Y-%m-%d')
        log_path = os.path.join("data", "logs", "log.csv")
        with open(log_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, subject, task, duration_minutes, productivity, notes])

        print(f"Logged {duration_minutes} minutes for {subject}: {task}. Session complete.")

        # Ask if user wants to log another session
        if input("Log another session? (y/N): ").strip().lower() != 'y':
            break


# Add headers if the file is empty or doesn't exist
log_path = os.path.join("data", "logs", "log.csv")
try:
    with open(log_path, "r") as file:
        if file.read().strip() == "":
            raise FileNotFoundError
except FileNotFoundError:
    with open(log_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Subject", "Task", "Duration (min)", "Productivity", "Notes"])


# Start logging
log_study()
