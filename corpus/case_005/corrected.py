def can_manage(actor, item):
    return actor.get('role') == 'admin' and actor.get('tenant') == item.get('tenant')
