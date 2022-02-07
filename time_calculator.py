def add_time(start, duration, startingDay=''):

  # separate start into integer variables (hour, minute) and store the period "AM/PM"
  startHour, startMinute = [int(item) for item in start[:-3].split(':')]
  startPeriod = start[-2:]

  # separate duration into integer variables (hours, minutes)
  durationHours, durationMinutes = [int(item) for item in duration.split(':')]

  # convert startingDay to lowercase and then capitalize so we can compare it later
  startingDay = startingDay.lower().capitalize()

  # convert the startHour to 24 hour format
  if startPeriod == 'PM' and startHour != 12:
    startHour += 12

  # add the minutes together for later calculation
  totalMinutes = startMinute + durationMinutes

  # add the start and duration hours, then add the hours gained from adding minutes
  totalHours = startHour + durationHours + (totalMinutes//60)

  # get the remaining minutes after removing the hours gained
  endMinutes = totalMinutes % 60

  # get the total days later
  totalDays = totalHours // 24

  # convert the hours back to 12hr time
  endHour = (totalHours % 24) % 12
  endHour = 12 if endHour == 0 else endHour

  # get the period
  endPeriod = 'AM' if ((totalHours % 24) <= 11) else 'PM'

  # create the end time string
  endTime = str(endHour) + ':' + str(endMinutes).zfill(2) + ' ' + endPeriod

  daysOfWeek = {
    "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6
  }

  if (startingDay != ''):
    endDay = (daysOfWeek[startingDay] + totalDays) % 7
    for key, value in daysOfWeek.items():
      if endDay == value:
        endDay = ', ' + key
        break
  else:
    endDay =  ''

  if (totalDays == 1):
    endXDays = ' (next day)'
  elif (totalDays > 1):
    endXDays = ' (' + str(totalDays) + ' days later)'
  else:
    endXDays = ''

  new_time = endTime + endDay + endXDays

  return new_time