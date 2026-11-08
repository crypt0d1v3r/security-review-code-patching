def may_update(actor, item):
    return actor.get('id') == item.get('owner')
