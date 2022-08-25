"""
The date module implements basic date and time functions.
"""

import datetime
qolang_export = {
    "func_format": "format",
    "func_current": "current",
    "timezones.func_get": "timezones.date",
    "timezones.func_now": "timezones.now",
    "timezones.func_full": "timezones.datetime"
}


def func_format(args: list):
    """
    format(date, format)\n
    Format UNIX timestamp.
    """
    return (datetime.datetime.utcfromtimestamp(args[0]).strftime(args[1]))


def func_current():
    """
    current()\n
    Get current date as UNIX timestamp.
    """
    return (datetime.datetime.now().timestamp())

class timezones:
 """
 timezones.class.function(offset)\n
 The timezones class provides basic functions for time offsets.
 """
 def func_get(offset):
    """
   timezones.date(offset)\n
   Get current date in a timezone.
    """
    return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=offset))).strftime("%D")
 def func_now(offset):
     """
   timezones.now(offset)\n
   Get current time in a timezone.
     """
     return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=offset))).strftime("%H:%M:%S")
 def func_full(offset):
   """
   timezones.datetime(offset)\n
   Get both time and date in a timezone.
   """
   return (datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=offset))).strftime("%D\n%H:%M:%S"))