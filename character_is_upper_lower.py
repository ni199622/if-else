#  The given character is an uppercase letter or lowercase letter or a digit or a special character.

char =input("enter character:")
if char>='A' or char>='B' or char>='a' or char>='b' :
 uppercase="char"
 lowercase="char"
 print("uppercase is", char)
 print("lowercase is", char)
elif char>=0 or char>=9:
  digit="char"
  print("digit is",char)
elif char=='@' or char=='#' or char=='$' or char=='%' or char=='&' or char=='*':
  special_character=char
  print("special_characte is")


