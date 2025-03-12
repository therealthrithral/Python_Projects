def add_time(start, duration, day='none'):
    # Split input variables into usable numbers
    start = start.split(':')
    duration = duration.split(':')
    start_hrs = int(start[0])
    start_mins = int(start[1].split(' ')[0])
    start_am_pm = start[1].split(' ')[1]
    duration_hrs = int(duration[0])
    duration_mins = int(duration[1])

    # Convert to 24 hour time
    if start_am_pm.lower() == 'pm': start_hrs = start_hrs + 12

    new_hrs = start_hrs + duration_hrs
    new_mins = start_mins + duration_mins
    days_later = 0

    # Check if minutes under 60 and hours adjust for extra 60 mins
    while new_mins > 59:
        new_mins = new_mins - 60
        new_hrs = new_hrs + 1

    # Check if hours under 23 and days get adjust for extra 24 hrs
    while new_hrs > 23:
        new_hrs = new_hrs - 24
        days_later = days_later + 1

    # Convert back to 12 hour time
    if new_hrs > 12:
        new_hrs = new_hrs - 12
        new_am_pm = 'PM'
    elif new_hrs == 12:
        new_am_pm = 'PM'
    else:
        new_am_pm = 'AM'

    # American adjustment (we are sorry!)
    if new_hrs == 0 and new_am_pm == 'AM':
        new_hrs = 12

    # Build new Time String
    new_time = str(new_hrs) + ':' + str(new_mins).zfill(2) + ' ' + new_am_pm

    if day != 'none':
        days = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ]
        day = day.lower().title()
        index = days.index(day)
        # Wrap around list to find new day
        new_index = (index + days_later) % len(days)
        # Add day to Time String
        new_time = new_time + ', ' + days[new_index]

    # Add number of days to Time String
    if days_later == 1:
        new_time = new_time + ' (next day)'
    elif days_later > 1:
        new_time = new_time + ' (' + str(days_later) + ' days later)'

    return new_time


print(add_time("8:16 PM", "466:02", "saturDay"))

