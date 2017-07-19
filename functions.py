from os import listdir, path, walk

def get_files(dir):
    names = [name for name in listdir(dir)
             if path.isfile(path.join(dir,name))]
    return names

def test_walk(dir):
    for root, dirs, files in walk(dir, topdown=False):
        print (root)

def populate(dir, type, cuantity):
    x=0
    while x<=int(cuantity):
        open(path.join(dir, 'populated'+str(x)+'.'+type), 'w')
        x+=1
