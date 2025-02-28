import os
import sys
import subprocess


def get_virtual_env_python():
    # Get the path to the Python interpreter in the virtual environment.
    if sys.platform == "win32":
        return os.path.join(".env", "Scripts", "python.exe")
    else:
        return os.path.join(".env", "bin", "python")


def main():
    # Get the path to the virtual environment's Python interpreter
    python_path = get_virtual_env_python()

    while True:
        print("\n=== Study Tracker ===")
        print("1. Log Study Session")
        print("2. Analyze Study Data")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            print("\nLogging Study Session...")
            subprocess.run([python_path, "scripts/study_tracker.py"])
        elif choice == "2":
            print("\nAnalyzing Study Data...")
            subprocess.run([python_path, "scripts/analyze_study.py"])
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
