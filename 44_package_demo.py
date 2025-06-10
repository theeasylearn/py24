#how to import module from package
# from package import module 
from earth import asia 
from earth import north_america as na 
from earth import europe as e 
# OR
# import earth.asia 
# import earth.europe as e 
# import earth.north_america as na 

print(asia.getCountries())
print(e.getCountries())
print(na.getCountries())
