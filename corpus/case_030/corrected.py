def valid_quota(value):
    return type(value) is int and 1 <= value <= 10
