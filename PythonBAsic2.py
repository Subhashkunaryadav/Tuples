#Tuples

t = ("Disco", 12, 4.5)
print(t)

# Single value tuples
sample_tuple = 1, #This is tuple
print(sample_tuple)
sample_tuple = (1,)  #This is tuple
print(sample_tuple)

sample_tuple = 1 #This is not a tuple
sample_tuple = (1) # This is not a tuple

#Indexing in tuples

t = ('mumbai', '45', 'python')
print(t[1])
print(t[-1])

#slicing

t = ('mumbai', '45', 'python', 'goa', '34', 'asus')
print(t[0:3])

t = ('mumbai', '45', 'python', 'goa', '34', 'asus')
print(t[-2:])

t = ('mumbai', '45', 'python', 'goa', '34', 'asus')
print(len(t))

#Concatenating tuples
t1 = ('This', 'is', 'the' )
t2 = ('second', 'tuples', 'in', 'python')
t3 = t1 + t2
print(t3)

x=(1,2,3)
print(x[2])

#sum(), min(), max()
t = (1,2,3,4,5,6)
tuples = sum(t)
print(tuples)

t = (1,2,3,4,5,6)
tuples = min(t)
print(tuples)

t = (1,2,3,4,5,6)
tuples = max(t)
print(tuples)

#immutability of tuples
#t = ('usa', '4', '3', 'disco', '7.5')
#add = t[3] = 'hard core'  # There will be an error because it cannot be changed

t = ('usa', '4', '3', 'disco', '7.5')
new = t[0:3] + ('hard rock',) + t[4:]
print(new)

#sorting tuples
t = (3,4,8,2,9,1,0,5)
note = sorted(t)
print(note)
x = sorted(t)
print(tuple(x))

#nested tuples
t = ('usa', '4', '3', ('disco', '7.5'))
print(t[3][1])

#packing and unpacking
t = (2,4,6,4)
(a,b,c,d) = t
print(a)

t = ()
print(dir(t))