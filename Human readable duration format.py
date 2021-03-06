# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

seconds_dict = {"second": 1,
                "minute": 60,
                "hour": 3600,
                "day": 86400,
                "year": 31536000,
                }


def format_duration(seconds):
    rem = seconds

     #Years
    years = (rem / seconds_dict["year"])
    if years >= 1:
        out_years = int(years)
        rem = years - out_years
        rem = seconds_dict["year"] * rem
    else:
        out_years = 0

    # Days
    days = (rem / seconds_dict["day"])
    if days >= 1:
        out_days = int(days)
        rem = days - out_days
        rem = seconds_dict["day"] * rem
    else:
        out_days = 0

    # hours
    hours = (rem / seconds_dict["hour"])
    if hours >= 1:
        out_hours = int(hours)
        rem = hours - out_hours
        rem = seconds_dict["hour"] * rem
    else:
        out_hours = 0

    # minutes
    minutes = (rem / seconds_dict["minute"])
    if minutes >= 1:
        out_minutes = int(minutes)
        rem = minutes - out_minutes
        rem = seconds_dict["minute"] * rem
    else:
        out_minutes = 0

    seconds = int(rem)

    print("{}, {}, {}, {}, {}".format(out_years, out_days, out_hours, out_minutes, seconds))
    return out_years, out_days, out_hours, out_minutes, seconds


def build_string():

    # TODO: build output string
    pass


def main():
    print(format_duration(62))
    print(format_duration(3662))
    print(format_duration(41536568))


if __name__ == '__main__':
    main()
