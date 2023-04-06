from matplotlib import pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

file_name = "data.txt"
string_to_add = "added"
start_year = 2022

# Adds zeros to format dates correctly
def datify(line):
    day_str_len = line.find('/')
    month_str_len = len(line) - line.find('/') - 1
    if day_str_len == 1:
        line = '0' + line
    if month_str_len == 1:
        line = line[:-1] + '0' + line[-1]
    return line

# Add year to en of dates
def add_year(dates, start_year):
    year = start_year
    full_dates = []
    for i in range(len(dates)):
        if i > 0 and int(dates[i-1][-2:]) > 1 and int(dates[i][-2:]) == 1: # Increment year from first date of january every year
            year += 1
        year_str = str(year)
        full_dates.append(dates[i] + '/' + year_str)
    return full_dates

# Format dates data
with open(file_name, 'r') as f:
    dates = [datify(x[5:].strip()) for x in f.readlines()]
full_dates = add_year(dates,start_year)
full_dates = [dt.datetime.strptime(d,'%d/%m/%Y').date() for d in full_dates]

# Format weight data
with open(file_name, 'r') as f:
    weights = [float(x[:4].replace(',','.')) for x in f.readlines()]

# Plot
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=45))
plt.ylabel('kg')
plt.title('Bodyweight')
plt.plot(full_dates, weights)
plt.gcf().autofmt_xdate()
plt.savefig('weight.png')


