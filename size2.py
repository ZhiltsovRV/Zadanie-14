import os

def get_size(path):
    size = 0
    if os.path.isfile(path):
        size = os.path.getsize(path)
    else:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                fp = os.path.join(dirpath, filename)
                if os.path.isfile(fp):
                    size += os.path.getsize(fp)
    return size

def human_readable_size(size):
    return size


def main():
    pwd = os.getcwd()
    items = os.listdir(pwd)
    size_list = []

    for item in items:
        full_path = os.path.join(pwd, item)
        size = get_size(full_path)
        size_list.append((size, item))
        #print("{} {}".format(size, item))

    size_list.sort(key=lambda x: x[0], reverse=True)

    for size, item in size_list:
        print("{} {}".format(size, item))

if __name__ == "_main_":
    main()