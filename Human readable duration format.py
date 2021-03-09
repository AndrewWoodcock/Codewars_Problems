# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

seconds_dict = {"second": 1,
                "minute": 60,
                "hour": 3600,
                "day": 86400,
                "year": 31536000,
                }


words_dict = {"s": ["second", "seconds"],
              "m": ["minute", "minutes"],
              "h": ["hour", "hours"],
              "d": ["day", "days"],
              "y": ["year", "years"]
              }


def primary(seconds):
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

    seconds = round(rem)

    # print("{}, {}, {}, {}, {}".format(out_years, out_days, out_hours, out_minutes, seconds))
    return out_years, out_days, out_hours, out_minutes, seconds


def build_string(durations):

    build_cnt = (len(durations) - durations.count(0))

    # TODO: build output string
    out_string = ""
    # years
    if durations[0] > 0:
        if durations[0] == 1:
            out_string = out_string + " " + str(durations[0]) + " " + words_dict["y"][0]
        else:
            out_string = out_string + " " + str(durations[0]) + " " + words_dict["y"][1]
        build_cnt -= 1
        if build_cnt > 1:
            out_string = out_string + ","
        else:
            if sum(durations[1:]) > 0:
                out_string = out_string + " and"

    # days
    if durations[1] > 0:

        if durations[1] == 1:
            out_string = out_string + " " + str(durations[1]) + " " + words_dict["d"][0]
        else:
            out_string = out_string + " " + str(durations[1]) + " " + words_dict["d"][1]
        build_cnt -= 1
        if build_cnt > 1:
            out_string = out_string + ","
        else:
            if sum(durations[2:]) > 0:
                out_string = out_string + " and"

    # hours
    if durations[2] > 0:

        if durations[2] == 1:
            out_string = out_string + " " + str(durations[2]) + " " + words_dict["h"][0]
        else:
            out_string = out_string + " " + str(durations[2]) + " " + words_dict["h"][1]
        build_cnt -= 1
        if build_cnt > 1:
            out_string = out_string + ","
        else:
            if sum(durations[3:]) > 0:
                out_string = out_string + " and"

    # minutes
    if durations[3] > 0:

        if durations[3] == 1:
            out_string = out_string + " " + str(durations[3]) + " " + words_dict["m"][0]
        else:
            out_string = out_string + " " + str(durations[3]) + " " + words_dict["m"][1]
        build_cnt -= 1
        print(build_cnt)
        if build_cnt > 1:
            out_string = out_string + ","
        else:
            if sum(durations[4:]) > 0:
                out_string = out_string + " and"

    # seconds
    if durations[4] > 0:
        if durations[4] == 1:
            out_string = out_string + " " + str(durations[4]) + " " + words_dict["s"][0]
        else:
            out_string = out_string + " " + str(durations[4]) + " " + words_dict["s"][1]

    return out_string.strip()


def format_duration(seconds):
    if seconds == 0:
        return "now"
    durations = primary(seconds)
    return build_string(durations)


print(format_duration(9225879))
