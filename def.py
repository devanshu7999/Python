#helloworld-fn
def hello():
    print("Hello World")

hello() #calling a function hello 


#sum-fn
def calc_sum(a, b): #parameters a and b pass 
    sum = a + b 
    print(sum)
    return sum
   
calc_sum(1,2) #3 -- function call

calc_sum(3,7) #10 -- function call

#avg-fn
def avg(a, b, c):
    avg = (a + b + c) / 3
    print(avg)
    return avg

avg(1,2,3) #2.0 -- function call


#length-fn
fruits =["apple", "banana", "cherry"]
def p_length(list):
    print(len(list))
    return len(list)

p_length(fruits) #3 -- function call

#factorial-fn
def cal_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
        print(fact)

cal_fact(3) #1*2*3=6 --function call

#variable-arguments
def varargs(*args):
    print(args)
    return args

varargs(1, 2, 3)  # => (1, 2, 3)

#Keyword-arguments
def keyword_args(**kwargs):
    print(kwargs)
    return kwargs

keyword_args(big="foot", loch="ness")
# => {"big": "foot", "loch": "ness"}

#Swapping
def swap(x, y):
    x, y = y, x
    print(x,y)
    return y, x
    
x = 1
y = 2
x, y = swap(x, y)  # => x = 2, y = 1

