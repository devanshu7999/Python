str = input('Enter your sentance : ')

l = [i for i in str.split(' ') if i[0:1] == 'h' or i[0:1] == 'H']
print(l)