def can_access(member, entry):
    return member.get('id') == entry.get('author')
