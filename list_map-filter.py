 #filter
l=[12,34,24,56,56]
def check(val):
    return not(val%12)
print(list(filter(check, l))) #o/p [12,24]


#map
l=[12,34,24,56,56]
def check(val):
    return not(val%12)         #[12,  ,      ,24   ,     ,     ]
print(list(map(check, l))) #o/p [True, False, True, False, False]