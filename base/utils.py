_MONTHS = (
    "Jan",
    "Feb",
    "March",
    "Apr",
    "May",
    "June",
    "July",
    "Aug",
    "Sept",
    "Oct",
    "Nov",
    "Dec",
)


def get_month(n):
    """Given an index n, returns corresponding month abbreviation"""
    return _MONTHS[n - 1]
