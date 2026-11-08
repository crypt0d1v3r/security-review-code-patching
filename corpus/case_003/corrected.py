def can_access(user, record):
    return user.get('workspace') == record.get('workspace') and user.get('id') == record.get('holder')
