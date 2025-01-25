from datetime import datetime

def sort_by_date(data, reverse=False):
    if reverse:
        sorted_data = sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=reverse)
    else:
        sorted_data = sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))
    return sorted_data