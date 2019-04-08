"""Constraints
1 ≤ work_hours ≤ 56
1 ≤ day_hours ≤ 8
| pattern | = 7
Each character of pattern ∈ {0, 1,...,8}
There is at least one correct schedule."""

def find_schedules(work_hours, day_hours, pattern):
    # Write your code here
    sched_hrs = 0
    #get current total scheduled hours
    for hour in pattern:
        if hour != '?':
            sched_hrs += int(hour)
    
    unsched_hrs = work_hours - sched_hrs
    new_pattern = ''
    for hour in pattern:
        if hour == '?':
            if unsched_hrs < day_hours:
                new_pattern += str(unsched_hrs) 
                unsched_hrs = 0
            elif unsched_hrs == 0:
                new_pattern += '0'
            else:
                unsched_hrs = unsched_hrs - day_hours
                new_pattern += str(day_hours)
        else:
            new_pattern += hour
    return new_pattern

# Test Case 1:
work_hours = 56
day_hours = 8
pattern = '??8????'
print find_schedules(work_hours, day_hours, pattern)

# Test Case 2:
work_hours = 3
day_hours = 2
pattern = '??2??00'
print find_schedules(work_hours, day_hours, pattern)

# Test Case 3:
work_hours = 5
day_hours = 3
pattern = '??2????'
print find_schedules(work_hours, day_hours, pattern)