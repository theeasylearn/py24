countries = [
    'Germany', 'Greenland', 'Ireland', 'Egypt', 'Spain', 'China', 'Iceland', 
    'Mexico', 'South Africa', 'India', 'Vietnam', 'Turkey', 'Switzerland', 
    'England', 'France', 'Argentina', 'Poland', 'Norway', 'Australia', 'Italy', 
    'Netherlands', 'Japan', 'Thailand', 'Brazil', 'South Korea', 'Saudi Arabia', 
    'New Zealand', 'Kenya', 'Canada', 'Finland'
]
# countries2 = [] #empty list
# for country in countries:
#     if 'land' in country:
#         countries2.append(country)
# print(countries2)
countries2 = filter(lambda country: 'land' in country,countries)
print(list(countries2))