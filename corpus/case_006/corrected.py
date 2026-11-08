def can_manage(principal, document):
    return principal.get('role') == 'admin' and principal.get('org') == document.get('org')
