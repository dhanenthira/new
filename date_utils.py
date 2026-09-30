from datetime import datetime, timedelta

def get_current_time():
    return datetime.now()

def add_days(dt, days):
    return dt + timedelta(days=days)

def format_date(dt, format_string="%Y-%m-%d %H:%M:%S"):
    return dt.strftime(format_string)
