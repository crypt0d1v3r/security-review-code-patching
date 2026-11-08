def may_update(member, entry):
    return member.get('id') == entry.get('author')
