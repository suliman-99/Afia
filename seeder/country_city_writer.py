import geonamescache
from unidecode import unidecode as _
gc = geonamescache.GeonamesCache()

countries_names = []
cities = []

for city_id, city_info in gc.get_cities().items():

    country_name = _(gc.get_countries().get(city_info.get('countrycode')).get('name'))
    city_name = _(city_info.get('name'))

    if ',' in city_name or ',' in country_name:
        continue
    
    countries_names.append(country_name)
    cities.append((city_name, country_name))


countries_names = list(set(countries_names))
cities = list(set(cities))

with open('Country.csv', 'w', encoding='utf-8') as country_file:
    country_file.write('name\n')
    for country_name in countries_names:
        country_file.write(country_name + '\n')

with open('City.csv', 'w', encoding='utf-8') as city_file:
    city_file.write('name,country_id\n')
    for city in cities:
        city_name = city[0]
        country_name = city[1]
        city_file.write(city_name + ',' + country_name + '\n')
