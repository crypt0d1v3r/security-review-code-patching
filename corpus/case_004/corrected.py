def can_access(member, entry):
    return member.get('account') == entry.get('account') and member.get('id') == entry.get('author')
