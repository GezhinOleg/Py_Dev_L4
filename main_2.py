import hashlib


def compute_MD5_hash(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            yield hashlib.md5(line.strip().encode('utf-8')).hexdigest()


if __name__ == '__main__':
    for md5 in compute_MD5_hash('outfile.txt'):
        print(md5)
