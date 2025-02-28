# Study Tracker

A Python-based tool to log and analyze your study sessions. Track your progress, visualize your study habits, and improve your productivity!

---

## Features

- **Log Study Sessions**: Record the subject, task, duration, productivity, and notes for each study session.
- **Weekly Reports**: Generate summaries and visualizations for each week.
- **Global Summary**: Aggregate data from all weeks into a single Markdown file.
- **Customizable**: Add your own subjects and customize the analysis.

---

## Directory Structure

```
study_tracker/
├── .env/                  # Virtual environment
├── scripts/               # Python scripts
│   ├── study_tracker.py   # Log study sessions
│   ├── analyze_study.py   # Analyze and generate reports
├── data/                  # Data and reports
│   ├── logs/              # Study session logs
│   │   ├── log.csv        # Main log file
│   ├── weekly_reports/    # Weekly reports
│   │   ├── YYYY-MM-DD/    # Weekly report folder
│   │   │   ├── study_summary.md
│   │   │   ├── study_time_by_subject.png
│   │   │   ├── productivity_over_time.png
│   │   │   ├── daily_study_time.png
│   ├── global_summary.md  # Aggregated summary of all weeks
├── requirements.txt       # Pip dependencies
├── setup.sh               # Setup script for Linux/Mac
├── setup.bat              # Setup script for Windows
├── run.py                 # User-friendly interface
├── README.md              # Project documentation
```

---

## Setup

### 1. Install Python and Pip
Ensure Python and Pip are installed on your system.

- **On Arch Linux**:
```bash
sudo pacman -S python python-pip
```

- **On Windows**:
  1. Download and install Python from the [official Python website](https://www.python.org/downloads/).
  2. During installation, ensure you check the box that says **"Add Python to PATH"**.
  3. Verify the installation by opening a Command Prompt and running:
```bash
python --version
pip --version
```

---

### 2. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/Kamel-CS/study_tracker.git
cd study_tracker
```

---

### 3. Run the Install Script
Run the appropriate install script for your operating system.

- **On Linux/Mac**:
```bash
./setup.sh
```

- **On Windows**:
```bash
setup.bat
```

---

### 4. Run the App
Start the app with a simple command:
```bash
python run.py
```

---

## Usage

### 1. Log Study Sessions
The `study_tracker.py` script to logs your study session:

Follow the prompts to enter:
- Subject
- Task
- Duration
- Productivity (1-10)
- Notes (optional)

### 2. Analyze and Generate Reports
The `analyze_study.py` script generates weekly and global summaries:

This will:
- Create a weekly report folder under `data/weekly_reports/YYYY-MM-DD/`.
- Update the global summary file (`data/global_summary.md`).

### 3. View Reports
- **Weekly Reports**: Check the `data/weekly_reports/YYYY-MM-DD/` folder for Markdown summaries and graphs.
- **Global Summary**: View the aggregated data in `data/global_summary.md`.

---

## Weekly Analysis

The `analyze_study.py` script is designed to run **only after 7 consecutive days of data** has been collected. Here’s how it works:

1. **Check for 7 Consecutive Days**:
   - The script checks if there’s data for **7 consecutive days** in the log.
   - If not, it will exit with a message: `"Not enough data for a complete week (7 consecutive days). Please log data for all 7 days."`

2. **Generate Weekly Report**:
   - If there’s enough data, the script generates a report for the **last 7 days**.
   - The report includes:
     - Total study time.
     - Average productivity.
     - Study time by subject.
     - Graphs for study time, productivity, and daily study time.

3. **Delete Log File**:
   - After generating the report, the `log.csv` file is deleted to start fresh for the next week.

---

## Customization

### Add or Modify Subjects
Edit the `SUBJECTS` list in `scripts/study_tracker.py` to include your own subjects:
```python
SUBJECTS = ["Project", "ICN", "IIS", "LT", "HT", "IDB", "OOP2"]
```

### Change Graph Colors
Update the `SUBJECT_COLORS` dictionary in `scripts/analyze_study.py` to customize the colors for each subject:
```python
SUBJECT_COLORS = {
    "Project": "blue",
    "ICN": "green",
    "IIS": "red",
    "LT": "purple",
    "HT": "orange",
    "IDB": "cyan",
    "OOP2": "magenta",
}
```

---

## Dependencies

- Python 3.x
- pandas
- matplotlib
- tabulate

Install them using:
```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
