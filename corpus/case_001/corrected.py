def can_access(actor, item):
    return actor.get('tenant') == item.get('tenant') and actor.get('id') == item.get('owner')
