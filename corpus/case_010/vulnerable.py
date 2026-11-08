def may_update(principal, document):
    return principal.get('id') == document.get('creator')
