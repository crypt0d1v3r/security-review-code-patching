def can_manage(member, entry):
    return member.get('role') == 'admin'
