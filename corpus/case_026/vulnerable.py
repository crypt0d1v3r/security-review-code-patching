def valid_quota(value):
    return isinstance(value, int) and 1 <= value <= 10
