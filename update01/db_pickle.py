import pickle

dbfilename= 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, dbfilename = dbfilename):
    #save to DB
    dbfile = open(dbfilename, 'wb')
    pickle.dump(db,dbfile)
    dbfile.close()
    """dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name,value) in db[key].items():
            print(name + RECSEP + repr(value), file= dbfile)
        print(ENDREC, file= dbfile)
    print(ENDDB, file= dbfile)
    dbfile.close()"""

def loadDbase(dbfilename = dbfilename):
    #load from file
    dbfile = open(dbfilename, 'rb')
    db = pickle.load(dbfile)
    for key in db:
        print(key, '=>\n', db[key])
    #print(db['sue']['name'])
    return db
"""    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key!= ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()"""

if __name__== '__main__':
    from initdata import db
    storeDbase(db)
    print(loadDbase())
