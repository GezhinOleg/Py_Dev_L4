import json
from pprint import pprint


class CountryIterate:

    def __init__(self, start, end, interval_size = 2):
        self.start = start - interval_size
        self.end = end
        self.interval_size = interval_size

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.interval_size
        if self.start >= self.end:
            raise StopIteration
        return self.start


def main():
    my_range = CountryIterate(1, 10)
    for country in my_range:
        print(country)

if __name__ == '__main__':
    main()