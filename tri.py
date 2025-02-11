def TriangleIdentification(side1,side2,side3):
    sides = [side1, side2, side3]
    sides.sort()
    medium = sides[1]
    maximum = sides[2]
    minimum = sides[0]
    print(maximum)
    print(medium)
    print(minimum)
    if side1==side2==side3:
        type="equilateral"
        return type
    elif (side1==side2 or side2==side3 or side1==side3) and not(side1==side2==side3):
        type="Isosceles"
        return type
    elif not(side1==side2) and not (side2==side3) and not(side1==side3) and not (maximum > medium + minimum):
        type="scalene"
        return type
    else :(maximum > medium + minimum)
    type = "invalid"
    return type

def main():
    print(f"{TriangleIdentification(3, 3, 3)}")

main()

#co pilot help == use of .sort() method to sort the sides of the triangle
# original code below
# 
# def mediummaker(side1,side2,side3):
#     maximum = max(side1,side2,side3)
#     minimum = min(side1,side2,side3)
#     sizes = (side1,side2,side3)
#     largeloss = sizes.remove({maximum})
#     medium = largeloss.split({minimum})
#     print(medium)
#     return medium
# def main():
#     mediummaker(3,3,3)
#     TriangleIdentification(sidel,side2,side3,maximum,medium,minimum)
#     print({type})
# main()

#test2()
#assert TriangleIdentification(3,3,3) == "equilateral"
#assert TriangleIdentification(3,3,4) == "Isosceles"
#assert TriangleIdentification (3,4,5) == "scalene"
#assert TriangleIdentification(3,3,7) == "invalid"