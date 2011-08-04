from mapreduce import operation as op
def process(entity):
 yield op.db.Delete(entity)