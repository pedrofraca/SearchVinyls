from mapreduce import operation as op
def process(entity):
    entity.num_items=len(entity.items)
    yield op.db.Put(entity)
