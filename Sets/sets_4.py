n = int(raw_input())
COUNTRY = set()
for i in range(n):
    country_name = raw_input()
    COUNTRY.add(country_name)
print len(COUNTRY)