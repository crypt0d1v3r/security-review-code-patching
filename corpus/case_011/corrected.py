def may_update(user, record):
    return user.get('current') is True and user.get('id') == record.get('holder')
