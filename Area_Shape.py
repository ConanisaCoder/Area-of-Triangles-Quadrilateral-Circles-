import math
shape = input("C= Circle, T = Triangle, Q = Quadrilateral: ")
if shape == "C":
    W = input ("D = Diameter, R = Raduis, C = Circumfrence :")
    if W == "D":
        diameter = input("What is the dimeter of a cirlce: ")
        diameter = (float(diameter))
        Area = (math.pi *pow(diameter,2))/4
        Area_rounded = round(Area)
        print(f"The Area of this Cirlce is {Area} units² ")
        print(f"The Area of this Cirlce rounded is {Area_rounded} units² ")
        Done = input("Press Enter When You Are Done: ")
    elif W == "R":
        raduis = float(input("What is the Raduis of the Cirlce: "))
        Area = math.pi * pow(raduis, 2)
        Area_rounded = round(Area)
        print(f"The Area of this Circle is {Area} units²    ")
        print(f"The Rounded Area of this Circle is {Area_rounded} units²    ")
        Done = input("Press Enter When You Are Done: ")
    elif W == "C":
        circumference = input("What is the circumference of the Circle: ")
        circumference = float(circumference)
        radius = (circumference/( 2* math.pi ))
        Area = math.pi * pow(radius, 2)
        Area_rounded = round(Area)
        print(f"The Area of this Circle is {Area} units²    ")
        print(f"The Rounded Area of this Circle is {Area_rounded} units²    ")
        Done = input("Press Enter When You Are Done: ")

elif shape == "T": 
    h = float(input("The Heigth of the triangle: "))
    b = float(input("The base of the Triangle:"))

    area = 1/2 * (h*b)
    print(f"The Area of the Traingle is {area} units²")
    Done = input("Press Enter When You Are Done: ")
elif shape == "Q": 
    Quad = input("K = Kite, T = Trapzoid, P = Parllogram: ")
    if Quad == "K" :
        d_1 = float(input("Length of Diagonal 1: "))
        d_2 = float(input("Length of diagonal 2: "))
        area = ((d_1*d_2)/2)
        print(f"The area of the Kite is {area} unit² ")
        Done = input("Press Enter When You Are Done: ")
    elif Quad == "T": 
        l_1 = float(input("What is the Length of The Top Side: "))
        l_2 = float(input("What is the Length of The Bottom Side: "))
        h = float(input("The Length of heigth of the Trapezoid: "))
        Area = (((l_1 + l_2)/2)*h)
        print(f"The area of the Trapezoid is {Area} unit² ")
        Done = input("Press Enter When You Are Done: ")
    elif Quad == "P":
        S_1 = float(input("Length of Side 1: "))
        S_2 = float(input("Length of Side 2: "))
        a = S_1 * S_1
        print(f"The area of the Parllogram is {a} unit² ")
        Done = input("Press Enter When You Are Done: ")
