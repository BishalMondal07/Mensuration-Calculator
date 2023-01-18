#It's supported figures are Circle,Square,Reectengle,Parallelogram,Rhombus,Trapezium,Cylinder,Cone,Sphere,Cube and Cuboid
#For Circle give input Radius in Length_or_Radius_or_Diagonal1
#For Triangle give input Base in Breadth_or_base_or_Diagonal2
#For Parallelogram in Perimeter give input of all four sides in four input sections
#For Rhombus give input diagonals in Length_or_Radius_Diagonal1 and Breadth_or_base_or_Diagonal2
#For Trapezium in Perimeter give input of all four sides in four input sections
#For Trapezium in Area give input of the Length of parallel sides in Length_or_Radius_Diagonal1 and Breadth_or_base_or_Diagonal2
#Give input "0" when input section doesn't require any input for any particular operation
#You can write Total Surface Area as TSA and Curved Surface Area as CSA in input
#All string inputs should start with capital letters but end with small letters (Example:Circle,Square,Total Surface Area)
#In Cone in Curved Surface Area and Total Surface Area give input radius in Breadth_or_base_or_Diagonal2 input section(Note: It is for cone only)
print("Read all the comments to use the calculator properly")
Figure = input("Enter the name of the figure :")
Length_or_Radius_or_Diagonal1 = int(input("Enter the value of Length or Radius or Diagonal 1:"))
Breadth_or_base_or_Diagonal2 = int(input("Enter the value of Breadth or Base or Diagonal2 :"))
Height_or_Other_side =  int(input("Enter the value of Height or Other side :"))
Other_side = int(input("Enter the value of Other side :"))
Operation = input("Enter the name of Operation :")
if (Figure == "Circle" and Operation == "Area") :
    print("Area of the Circle is" , Length_or_Radius_or_Diagonal1**2*22/7)
elif (Figure == "Circle" and Operation == "Circumference") :
    print("Circumference of the Circle is" , Length_or_Radius_or_Diagonal1*2*22/7)
elif (Figure == "Square" and Operation == "Area") :
    print("Area of the Square is" , Length_or_Radius_or_Diagonal1**2)
elif (Figure == "Square" and Operation == "Perimeter") :
    print("Perimeter of the Square is" , Length_or_Radius_or_Diagonal1*4)
elif (Figure == "Rectengle" and Operation == "Area") :
    print("Area of the Rectengle is" , Length_or_Radius_or_Diagonal1*Breadth_or_base_or_Diagonal2)
elif (Figure == "Rectengle" and Operation == "Perimeter") :
    print("Perimeter of the Rectengle is" , 2*(Length_or_Radius_or_Diagonal1+Breadth_or_base_or_Diagonal2))
elif (Figure == "Triangle" and Operation == "Area") :
    print("Area of the Triangle is" , Breadth_or_base_or_Diagonal2*1/2*Height_or_Other_side)
elif (Figure == "Triangle" and Operation == "Perimeter") :
    print("Perimeter of the Triangle is" , Length_or_Radius_or_Diagonal1+Breadth_or_base_or_Diagonal2+Height_or_Other_side)
elif (Figure == "Parallelogram" and Operation == "Area") :
    print("Area of the Parallelogram is" , Length_or_Radius_or_Diagonal1*Height_or_Other_side)
elif (Figure == "Parallelogram" and Operation == "Perimeter") :
    print("Perimeter of the Parallelogram is" , Length_or_Radius_or_Diagonal1+Breadth_or_base_or_Diagonal2+Height_or_Other_side+Other_side)
elif (Figure == "Rhombus" and Operation == "Area") :
    print("Area of the Rhombus is" , Length_or_Radius_or_Diagonal1*Breadth_or_base_or_Diagonal2*1/2)
elif (Figure == "Rhombus" and Operation == "Perimeter") :
    print("Perimeter of the Rhombus is" , Length_or_Radius_or_Diagonal1*4)
elif (Figure == "Trapezium" and Operation == "Area") :
    print("Area of the Trapeium is" , 1/2*(Length_or_Radius_or_Diagonal1+Breadth_or_base_or_Diagonal2)*Height_or_Other_side)
elif (Figure == "Trapezium" and Operation == "Perimeter") :
    print("Perimeter of the Trapezium is" , Length_or_Radius_or_Diagonal1+Breadth_or_base_or_Diagonal2+Other_side+Height_or_Other_side)
elif (Figure == "Cube" and Operation == "Volume") :
    print("Volume of the Cube is" , Length_or_Radius_or_Diagonal1**3)
elif (Figure == "Cube" and Operation == "Total Surface Area") :
    print("Total Surface Area of the Cube is" , 6*Length_or_Radius_or_Diagonal1**2)
elif (Figure == "Cube" and Operation == "Curved Surface Area") :
    print("Area of the Square is" , 4*Length_or_Radius_or_Diagonal1**2)
elif (Figure == "Cuboid" and Operation == "Volume") :
    print("Volume of the Cuboid is" , Length_or_Radius_or_Diagonal1*Breadth_or_base_or_Diagonal2*Height_or_Other_side)
elif (Figure == "Cuboid" and Operation == "Total Surface Area") :
    print("Total Surface Area of the Cuboid is" , 2*(Length_or_Radius_or_Diagonal1*Breadth_or_base_or_Diagonal2+Length_or_Radius_or_Diagonal1*Height_or_Other_side+Breadth_or_base_or_Diagonal2*Height_or_Other_side))
elif (Figure == "Cuboid" and Operation == "Curved Surface Area") :
    print("Curved Surface Area of the Cuboid is" , 2*(Length_or_Radius_or_Diagonal1*Breadth_or_base_or_Diagonal2)*Height_or_Other_side)
elif (Figure == "Cylinder" and Operation == "Volume") :
    print("Volume of the Cylinder is" , Length_or_Radius_or_Diagonal1**2*22/7*Height_or_Other_side)
elif (Figure == "Cylinder" and Operation == "Curved Surface Area") :
    print("Area of the Cylinder is" , 2*22/7*Length_or_Radius_or_Diagonal1*Breadth_or_base_or_Diagonal2)
elif (Figure == "Cylinder" and Operation == "Total Surface Area") :
    print("Total Surface Area of the Cylinder is" , 2*22/7*Length_or_Radius_or_Diagonal1*(Length_or_Radius_or_Diagonal1+Height_or_Other_side))
elif (Figure == "Cone" and Operation == "Volume") :
    print("Volume of the Cone is" , (1/3)*22/7*Length_or_Radius_or_Diagonal1**2*Height_or_Other_side)
elif (Figure == "Cone" and Operation == "Curved Surface Area") :
    print("Curved Surface Area of the Cone is" , 22/7*Length_or_Radius_or_Diagonal1*Breadth_or_base_or_Diagonal2)
elif (Figure == "Cone" and Operation == "Total Surface Area") :
    print("Total Surface Area of the Cone is" , 22/7*Breadth_or_base_or_Diagonal2*(Length_or_Radius_or_Diagonal1+Breadth_or_base_or_Diagonal2))
elif (Figure == "Sphere" and Operation == "Volume") :
    print("Volume of the Sphere is" , (4/3)*22/7*Length_or_Radius_or_Diagonal1**3)
elif (Figure == "Sphere" and Operation == "Curved Surface Area") :
    print("Curved Surface Area of the Sphere is" , 4*22/7*Length_or_Radius_or_Diagonal1**2)
elif (Figure == "Sphere" and Operation == "Curved Surface Area") :
    print("Curved Surface Area of the Sphere is" , 4*22/7*Length_or_Radius_or_Diagonal1**2)