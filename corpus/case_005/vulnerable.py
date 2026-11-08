def can_manage(actor, item):
    return actor.get('role') == 'admin'
