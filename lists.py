thislist = ["apple", "banada", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist.insert(2, "watermelon")
print(thislist)


#extend adds an entire list to a previous one
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])


i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1


#using comprehension to loop through the lists in one line
[print(x) for x in thislist]


##adding to a new list based on conditions of values in the previous
newlist = []

for x in thislist:
    if "a" in x:
        newlist.append(x)

print(newlist)



#you can do the above quickly with comprehension too
#syntax = newlist = [expression for item in iterable if condition == True]
newlist = [x for x in thislist if "a" in x]

print(newlist)

newlist = [i for i in thislist if i == "mango"]

print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

#can also manipulate the expression:
newlist = [x.upper() for x in thislist]
print(newlist)

#can also contain conditions, this returns the item and adds to the list if the item is not apple, if it is apple adds orange
newlist = [x if x != "apple" else "orange" for x in thislist]
print(newlist)

#can sort...alphabetically or numerically
newlist.sort()
print(newlist)

#can sort descending - reverse = true
newlist.sort(reverse = True)
print(newlist)

#can also sort by a funtion to define...
def myfunc(n):
    print(n - 50)
    return abs(n - 50)

newlist = [100, 50, 65, 82, 23]
newlist.sort(key = myfunc)
print(newlist)

#by default lists sort upper case first, can also reverse the whole list
newlist.reverse()
print(newlist)

#copy list with .copy. cant use = because it will only be a reference, any changes made to initial list will be reflected in new
newnewlist = newlist.copy()
print(newnewlist)

#can join lists with +
newestlist = newnewlist + newlist
print(newestlist)

#can also just append with for loop
for x in newlist:
    newestlist.append(x)

print(newestlist)


print(newestlist.index(100))
