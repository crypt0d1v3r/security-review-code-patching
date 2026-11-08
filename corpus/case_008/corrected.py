def can_manage(member, entry):
    return member.get('role') == 'admin' and member.get('account') == entry.get('account')
