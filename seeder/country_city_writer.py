import pandas
import geonamescache
from unidecode import unidecode as _
gc = geonamescache.GeonamesCache()

# ----------------------------------------------------------------------------------------

countries_names = []
cities = []

for city_id, city_info in gc.get_cities().items():

    country_name = _(gc.get_countries().get(city_info.get('countrycode')).get('name'))
    city_name = _(city_info.get('name'))
    
    countries_names.append(country_name)
    cities.append((city_name, country_name))

# ----------------------------------------------------------------------------------------

countries_names = list(set(countries_names))

countries_data = {}
countries_data['name'] = []

for country_name in countries_names:
    countries_data['name'].append(country_name)
    
country_file = pandas.DataFrame(countries_data)
country_file.to_csv('country.csv', index=False)

# ----------------------------------------------------------------------------------------

cities = list(set(cities))

city_data = {}
city_data['name'] = []
city_data['country_id'] = []

for city in cities:
    city_data['name'].append(city[0])
    city_data['country_id'].append(city[1])

city_file = pandas.DataFrame(city_data)
city_file.to_csv('city.csv', index=False)

# ----------------------------------------------------------------------------------------
