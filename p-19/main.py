import datetime


def count_days(start_year, end_year, day_of_month=1, weekday_index=6):
    count_sundays_on_first = 0
    for year in range(start_year, end_year + 1, 1):
        for month in range(1, 13, 1):
            if datetime.date(year, month, day_of_month).weekday() == weekday_index:
                count_sundays_on_first += 1

    return count_sundays_on_first


if __name__ == '__main__':
    print(count_days(start_year=1901, end_year=2000))
