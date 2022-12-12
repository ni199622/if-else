# find oldest ,middle and youngest numbers


a = int(input("enter 1st no. "))
b =int(input("enter 2nd no. "))
c = int(input("enter 3rd no. "))
if a>b and a>c:
    print(a,"oldest no.")
elif b>a and b>c:
    print(b,"oldest.")
else:
    print(c,"oldest")
if a>b and a<c:
    print(a,"middle")
elif b>a and b<c:
    print(b,"middle")
else:
    print(c,"middle")
if a<b and a<c:
  print(a,"youngest")
elif b<a and b<c:
  print(b,"youngest")
else:
  print(c,"youngest")