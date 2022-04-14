map_day = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday",5: "Thursday", 6: "Friday", 7: "Saturday"}

def add_time(start, duration, start_day = ""):

    new_time = ""
    day_of_week = 0
    # map day of the week with key value
    for key, value in map_day.items():
      if start_day.lower() == value.lower():
        day_of_week = key
        break

    # convert to integer
    # convert to 24 hour format
    time, format = start.split()
    hours, minutes = time.split(':')
    hours = int(hours)
    minutes = int(minutes)

    if format == "PM":
      hours+=12

    # convert to integer
    hour_duration, minute_duration = duration.split(':')
    hour_duration = int(hour_duration)
    minute_duration = int(minute_duration)

    # add up the duration to the start time
    final_hours = hours + hour_duration
    final_minutes = minutes + minute_duration
    days = 0

    # add up the hours
    while final_minutes >= 60:
      final_minutes = final_minutes - 60
      final_hours += 1
    # add up the days
    while final_hours >= 24:
      final_hours = final_hours - 24
      days += 1
      
    # convert back to 12 hour format
    if final_hours == 12 :
      format = "PM"
    elif final_hours > 12:
      format = "PM"
      final_hours -= 12
    elif final_hours == 0:
      format = "AM"
      final_hours += 12
    else :
      format = "AM"

    day_of_week = (day_of_week + days)%7

    # string formatting to match output
    if final_minutes < 10 :
      result_time = str(final_hours) + ":" + "0" + str(final_minutes) + " " + format
    else :
      result_time = str(final_hours) + ":" + str(final_minutes) + " " + format

    if days == 1:
      no_of_days = "(next day)" 
    elif days >=2:
      no_of_days = "(" + str(days) + " days" + " later" + ")"
    else:
      no_of_days = ""

    if len(start_day) == 0:
      new_time = result_time + " " + no_of_days
    else :
      new_time = result_time + ", " + map_day[day_of_week] + " " + no_of_days

    new_time = new_time.strip()
  
    return new_time
