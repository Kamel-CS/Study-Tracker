import pandas as pd
import matplotlib.pyplot as plt
import os

# Define your subjects and their colors
SUBJECT_COLORS = {
    "Project": "blue",
    "ICN": "green",
    "IIS": "red",
    "LT": "purple",
    "HT": "orange",
    "IDB": "cyan",
    "OOP2": "magenta",
}

# Create directories if they don't exist
os.makedirs("data/logs", exist_ok=True)
os.makedirs("data/weekly_reports", exist_ok=True)

# Load the study log
log_path = os.path.join("data", "logs", "log.csv")
try:
    log = pd.read_csv(log_path)
except FileNotFoundError:
    print("No study log found. Please run study_tracker.py first.")
    exit()

# Convert Date to datetime
log["Date"] = pd.to_datetime(log["Date"])

# Get all unique dates in the log
unique_dates = log["Date"].dt.date.unique()

# Sort the dates
unique_dates.sort()

# Check for 7 consecutive days
has_full_week = False
start_date = None
end_date = None

for i in range(len(unique_dates) - 6):
    # Check if the next 6 dates are consecutive
    if (unique_dates[i + 6] - unique_dates[i]).days == 6:
        has_full_week = True
        start_date = unique_dates[i]
        end_date = unique_dates[i + 6]
        break

if not has_full_week:
    print("Not enough data for a complete week (7 consecutive days).")
    exit()

# Filter log for the 7-day period
weekly_log = log[(log["Date"].dt.date >= start_date) & (log["Date"].dt.date <= end_date)]

# Analyze data
total_study_time = weekly_log["Duration (min)"].sum()
average_productivity = weekly_log["Productivity"].mean()
study_by_subject = weekly_log.groupby("Subject")["Duration (min)"].sum()

# Generate weekly summary text
weekly_summary_text = f"""
# Weekly Study Summary ({start_date} to {end_date})

**Total study time:** {total_study_time} minutes

**Average productivity:** {average_productivity:.2f}/10

## Study Time by Subject
{study_by_subject.to_string()}
"""

# Print weekly summary to terminal
print(weekly_summary_text)

# Create a weekly report folder
report_folder = os.path.join("data", "weekly_reports", end_date.strftime('%Y-%m-%d'))
os.makedirs(report_folder, exist_ok=True)

# Save weekly summary to a Markdown file
weekly_summary_file = os.path.join(report_folder, "study_summary.md")
with open(weekly_summary_file, "w") as f:
    f.write(weekly_summary_text)

# Plot study time by subject with custom colors
study_by_subject.plot(kind="bar", title="Study Time by Subject", color=[SUBJECT_COLORS.get(subj, "gray") for subj in study_by_subject.index])
plt.xlabel("Subject")
plt.ylabel("Total Study Time (minutes)")
plt.savefig(os.path.join(report_folder, "study_time_by_subject.png"))
plt.close()  # Close the plot

# Plot productivity over time
weekly_log.set_index("Date")["Productivity"].plot(kind="line", title="Productivity Over Time")
plt.xlabel("Date")
plt.ylabel("Productivity (1-10)")
plt.savefig(os.path.join(report_folder, "productivity_over_time.png"))
plt.close()  # Close the plot

# Plot daily study time
daily_study_time = weekly_log.groupby("Date")["Duration (min)"].sum()
daily_study_time.plot(kind="line", title="Daily Study Time")
plt.xlabel("Date")
plt.ylabel("Total Study Time (minutes)")
plt.savefig(os.path.join(report_folder, "daily_study_time.png"))
plt.close()  # Close the plot

# Generate global summary text
global_summary_file = os.path.join("data", "global_summary.md")
if os.path.exists(global_summary_file):
    with open(global_summary_file, "r") as f:
        global_summary_text = f.read()
else:
    global_summary_text = "# Global Study Summary\n\n"

# Append this week's data to the global summary
global_summary_text += f"""
## Week of {start_date} to {end_date}

**Total study time:** {total_study_time} minutes

**Average productivity:** {average_productivity:.2f}/10

### Study Time by Subject
{study_by_subject.to_string()}

---

"""

# Save global summary to a Markdown file
with open(global_summary_file, "w") as f:
    f.write(global_summary_text)

# Delete log.csv after analysis
os.remove(log_path)
print(f"Deleted log file: {log_path}")

print(f"Weekly report saved to: {report_folder}")
print(f"Global summary updated: {global_summary_file}")
