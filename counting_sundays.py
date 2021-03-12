import datetime


def countingSundays(startYear=1901, endYear=2000):
    firstOfMonthSundaysCount = 0
    for year in range(startYear, endYear+1):
        for month in range(1, 13):
            firstOfMonth = datetime.datetime(year, month, 1)
            if firstOfMonth.strftime('%A') == "Sunday":
                firstOfMonthSundaysCount += 1

    return firstOfMonthSundaysCount


print(countingSundays())
