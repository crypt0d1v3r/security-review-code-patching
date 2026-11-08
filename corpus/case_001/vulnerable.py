def can_access(actor, item):
    return actor.get('id') == item.get('owner')
