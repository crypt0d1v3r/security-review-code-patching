def may_update(member, entry):
    return member.get('valid') is True and member.get('id') == entry.get('author')
