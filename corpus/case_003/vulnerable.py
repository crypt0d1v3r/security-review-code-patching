def can_access(user, record):
    return user.get('id') == record.get('holder')
