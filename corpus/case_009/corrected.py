def may_update(actor, item):
    return actor.get('active') is True and actor.get('id') == item.get('owner')
