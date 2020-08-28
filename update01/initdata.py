bob = {'name': 'Bob Smith', 'age': 42, 'pay': 42000, 'job': 'software'}
sue = {'name': 'Sue Smid', 'age': 45, 'pay': 40000, 'job': 'hardware'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}

db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == "__main__":
    for key in db:
        print(key, '=>\n', db[key])

