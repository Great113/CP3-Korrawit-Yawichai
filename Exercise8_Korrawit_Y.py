Username = input("username : ")
Password = input("password : ")
if Username == "Korrawit" and Password == "K":
    print("Suscess")
    print("^^^^^^ JunShop ^^^^^^")
    print("---------------------")
    Apple = 30
    Banana = 20
    Mango = 45
    print("1.","Apple-30THB ")
    print("2.","Banana-20THB ")
    print("3.","Mango-45THB ")
    print("--------------")
    Selected = str(input("SelectedProduct :"))
    if Selected == "Apple":
       Number1  = int(input("Apple Amount : "))
       Total1   = Apple * Number1
       print(Total1,"THB")
       print("Thank for Buying :)")
    elif Selected == "Banana":
       Number2 = int(input("Amount Banana : "))
       Total2  = Banana * Number2
       print(Total2,"THB")
       print("Thank for Buying :)")
    elif Selected == "Mango":
       Number3 = int(input("Amount Mango : "))
       Total3 = Mango * Number3
       print(Total3, "THB")
       print("Thank for Buying :)")
    else:
        print("Sorry Please Try Again :)")
else:
    print("Sorry Please Try Again :)")