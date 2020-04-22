#Write a function which takes a list and integer k as parameters and then rotate that list by k
#Example, list = [1,2,3,4,5] and k = 3, it will return [4,5,1,2,3]
#k can be negative as well

def rotate(mylist, k):
  l2 = []
  if k >0:
    for i in range(len(mylist)-k, len(mylist)):
      l2.append(mylist[i])

    for j in range(0, len(mylist)-k):
      l2.append(mylist[j])

  elif k<0:
    l2.append(mylist[-k:]+mylist[:-k])
  
  return l2

rn1 = int(input("Enter the number from where rotate starts : "))
l1 = [1,2,3,4,5]

print(rotate(l1,rn1))
