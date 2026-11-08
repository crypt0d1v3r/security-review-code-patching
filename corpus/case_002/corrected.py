def can_access(principal, document):
    return principal.get('org') == document.get('org') and principal.get('id') == document.get('creator')
