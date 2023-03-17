from .words import ukr_to_lat
import re


def is_cyrillic(s):
    return bool(re.match('^[а-яА-ЯіІїЇєЄґҐ]+$', s))


def get_string(sting):
    if is_cyrillic(sting):
        converted_text = "".join([ukr_to_lat.get(c, c) for c in sting])
        if converted_text.lower().count('y') > 1:
            converted_text = converted_text.replace('y', '', 1)
        return converted_text
    return sting
