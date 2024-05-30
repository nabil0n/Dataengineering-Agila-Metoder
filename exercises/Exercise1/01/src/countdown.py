from datetime import datetime, timedelta
import pandas as pd

# Define the dates
events = {
    'summer_break': '2024-06-09 15:00',
    'lia_start': '2024-09-25 08:00',
    'christmas': '2024-12-24 00:00',
    'bellas_birthday': '2024-12-07 00:00',
    'new_year': '2025-01-01 00:00',
    'graduation_party': '2025-06-09 16:30'
}

# Convert event dates to datetime objects
event_dates = {event: datetime.strptime(date, '%Y-%m-%d %H:%M') for event, date in events.items()}

# Current datetime
current_time = datetime.now()

# Calculate the countdowns
countdowns = {event: event_date - current_time for event, event_date in event_dates.items()}

# Break down the countdowns into components
def breakdown_timedelta(delta):
    days, seconds = delta.days, delta.seconds
    years, days = divmod(days, 365)
    months, days = divmod(days, 30)
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return years, months, days, hours, minutes, seconds

breakdown = {event: breakdown_timedelta(delta) for event, delta in countdowns.items()}

# Create a dataframe
df = pd.DataFrame.from_dict(breakdown, orient='index', columns=['years', 'months', 'days', 'hours', 'minutes', 'seconds'])

# Display the dataframe
print("-------------------------------------------------------------")
print("Countdown from", current_time)
print("-------------------------------------------------------------")
print(df)