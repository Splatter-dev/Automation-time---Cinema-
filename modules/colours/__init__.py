def red(msg):
    msg = f'{colours["red"]}{msg}{colours["no_colour"]}'
    return msg


def blue(msg):
    msg = f'{colours["blue"]}{msg}{colours["no_colour"]}'
    return msg


def purple(msg):
    msg = f'{colours["purple"]}{msg}{colours["no_colour"]}'
    return msg


def yellow(msg):
    msg = f'{colours["yellow"]}{msg}{colours["no_colour"]}'
    return msg


def green(msg):
    msg = f'{colours["green"]}{msg}{colours["no_colour"]}'
    return msg


colours = {
    "red": "\033[31m",
    "yellow": "\033[33m",
    "purple": "\033[34m",
    "blue": "\033[36m",
    "green": "\033[32m",
    "no_colour": "\033[m"
}
