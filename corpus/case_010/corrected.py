def may_update(principal, document):
    return principal.get('enabled') is True and principal.get('id') == document.get('creator')
