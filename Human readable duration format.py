# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

seconds_dict = {"second": 1,
                "minute": 60,
                "hour": 3600,
                "day": 86400,
                "year": 31536000,
                }


words_dict = {"s": ["Second", "Seconds"],
              "m": ["minute", "minutes"],
              "h": ["hour", "hours"],
              "d": ["day", "days"],
              "y": ["year", "years"]
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


def build_string(durations):

    # TODO: build output string
    out_string = ""
    # years
    if durations[0] > 0:
        if durations[0] == 1:
            out_string = out_string + " " + str(durations[0]) + " " + words_dict["y"][0]
        else:
            out_string = out_string + " " + str(durations[0]) + " " + words_dict["y"][1]

    # days
    if durations[1] > 0:

        if durations[1] == 1:
            out_string = out_string + " " + str(durations[1]) + " " + words_dict["d"][0]
        else:
            out_string = out_string + " " + str(durations[1]) + " " + words_dict["d"][1]

    # hours
    if durations[2] > 0:

        if durations[2] == 1:
            out_string = out_string + " " + str(durations[2]) + " " + words_dict["h"][0]
        else:
            out_string = out_string + " " + str(durations[2]) + " " + words_dict["h"][1]

    # minutes
    if durations[3] > 0:

        if durations[3] == 1:
            out_string = out_string + " " + str(durations[3]) + " " + words_dict["m"][0]
        else:
            out_string = out_string + " " + str(durations[3]) + " " + words_dict["m"][1]

    # seconds
    if durations[4] > 0:
        if durations[4] == 1:
            out_string = out_string + " " + str(durations[4]) + " " + words_dict["s"][0]
        else:
            out_string = out_string + " " + str(durations[4]) + " " + words_dict["s"][1]


    print(out_string)


def main():
    durations = format_duration(41536568)
    # durations = format_duration(3662)
    build_string(durations)

    # print(format_duration(62))
    # print(format_duration(120))
    # print(format_duration(3662))
    # print(format_duration(41536568))


if __name__ == '__main__':
    main()
