import json

MAIN_LINK = 'https://en.wikipedia.org/wiki/'


class CountryIterate:

    def __init__(self, file_path, outfile):
        with open(file_path, encoding='utf-8') as country_files:
            self.country_names = json.load(country_files)
        self.outfile = outfile
        with open(self.outfile, 'w', encoding='utf-8') as out_file:
            out_file.write('')

    def __iter__(self):
        return self

    def __next__(self):
        if not self.country_names:
            raise StopIteration
        country = self.country_names.pop(0)
        name_country = country['name']['official']
        country_link = MAIN_LINK + name_country.replace(' ', '_')
        with open(self.outfile, 'a', encoding='utf-8') as out_file:
            out_file.write(f'{name_country} - {country_link} \n')
        return f'{name_country} - {country_link}'


def main():
    for country in CountryIterate('countries.json', 'outfile.txt'):
        print(country)


if __name__ == '__main__':
    main()
