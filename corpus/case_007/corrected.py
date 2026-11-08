def can_manage(user, record):
    return user.get('role') == 'admin' and user.get('workspace') == record.get('workspace')
