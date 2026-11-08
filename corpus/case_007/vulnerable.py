def can_manage(user, record):
    return user.get('role') == 'admin'
