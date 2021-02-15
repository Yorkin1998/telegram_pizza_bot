import geonamescache
import names
gc = geonamescache.GeonamesCache()
cities = gc.get_cities()

basket_for_cities = []
occured_name=[]
occured_city=[]
basket_for_names=set()
a = "Robert was killing the mokingbird in Bukhara , then Randy came to see him and said we should go to Tashkent , " \
    "After hearding this the John laughed at Thomas and said no we should not to Moscow we should go to Samarkand ," \
    "then they came to Shanghai to watch Leo "
x = a.split()

for i in range(0, 1000):
    k = names.get_first_name(gender='male')
    basket_for_names.add(k)
for i, m in cities.items():
    # print(m['name'])
    basket_for_cities.append(m['name'])
for i in x:
    if i in basket_for_names:
        occured_name.append(i)
    if i in basket_for_cities:
        occured_city.append(i)

print("UCHRAGAN ISMLAR:",occured_name)
print("UCHRAGAN SHAHARLAR:",occured_city)

