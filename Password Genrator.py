u = input("Enter Your Name: ")
p = input("Enter Your Password: ")
#Id1 = "Y"
#Id2 = "N"

if u == "jahid" and p == "12345" :
    print("You Can Access & Use This Features")

h = input("Enter Your Hints To Make PassWord To generate: ")
print("Your Password Is Generated:" + (str(len(h)) +  str(h[:2].lower()) + str(h[:1:-2].upper()) + "-" + str(h.count(h)) + str(h[:1].upper()) + "X"
+ "6" + "_" + "D" + str(h[0::3].lower()) + str(h.count(h)) + "X" + "f" + str(h[:4].lower()) + "+" + str(h[4::-1].upper())).strip().replace(" ", ""  ))


print("This Tool Create By - DJSAVI ")
# ---------------------------------------------------           



# else:
#     print("Your Username And PassWord Is Incorrect") 
#     print("If you Have no Access Id.")
#     hhh = input("You Create A New Id To Press Y Or N: ")  
# if hhh == "Y":
#     print("you Are Making A New Id")

# #
# if hhh == "N":
## print("You Cant Access It"

