# creat a dict. and make user to get values by  entering keys
dict={"Naam":"Name",
       "Kaam":"Work",
       "Ghar":"House"}
print("Enter any one out of these three: ", end=" ")
print(dict.keys())
a=input()
print("Engish translation of this word is " , end="")
print(dict.get(a))
