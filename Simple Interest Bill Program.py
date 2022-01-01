def calculate_SI():
    name = input("Enter your name: ")
    p = float(input("Enter Principal Amount : Rs. "))
    r = float(input("Enter Rate of Interest : "))
    n = int(input("Enter loan months : "))

    si = (p * n * r)/100
    amt = p + si
    
    print("")
    print("---------------------------")
    print("Calculating Simple Interest")
    print("---------------------------")
    print("Name :",name)
    print("")
    print("Principal Amount Rs. ",p)
    print("")
    print("Rate of Interest : ",r)
    print("")
    print("Number of months : ",n)
    print("")
    print("Simple Interest : Rs. ",si)
    print("")
    print("Amount : Rs. ",amt)
    print("")

calculate_SI()
