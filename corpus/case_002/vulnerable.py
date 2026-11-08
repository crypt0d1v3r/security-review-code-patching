def can_access(principal, document):
    return principal.get('id') == document.get('creator')
