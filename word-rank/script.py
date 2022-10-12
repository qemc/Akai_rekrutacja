import re
from collections import Counter


sentences = [
    'Taki mamy klimat mamy mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]
all = ''
for i in sentences:
    all = all+' '+ i
    
words = re.findall(r'\w+',all)
most = Counter(words).most_common()

print("1. " + str(most[0][0]) +" - "+ str(most[0][1]))
print("2. " + str(most[1][0]) +" - "+ str(most[1][1]))
print("3. " + str(most[2][0]) +" - "+ str(most[2][1]))

