def may_update(user, record):
    return user.get('id') == record.get('holder')
