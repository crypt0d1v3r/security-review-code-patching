def can_manage(principal, document):
    return principal.get('role') == 'admin'
