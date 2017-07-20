from os import listdir, path, walk, rename


def get_files(dir):
    names = [name for name in listdir(dir)
             if path.isfile(path.join(dir, name))]
    return names


def test_walk(dir):
    for root, dirs, files in walk(dir, topdown=False):
        print(root)


# Create x quantity of empty files on a specified directory, given the file extension.
def populate(dir, type, cuantity):
    x = 0
    while x <= int(cuantity):
        open(path.join(dir, 'populated ' + str(x) + '.' + type), 'w')
        x += 1


# Remove the first numbers of a string if it is a number or specified digits
def remove_first_numbers(string):
    digits = (' ', '.', '#')
    if string.isdigit():
        return 'This is not a string'
    while string[0].isdigit() or string[0] in digits:
        string = string[1:]
    return (string)


def fix_numbers_filenames(dir):
    c = 0
    for filename in listdir(dir):
        if rename(path.join(dir, filename), path.join(dir, remove_first_numbers(filename))):
            c += 1
    return 'Archivos Renombrados'
