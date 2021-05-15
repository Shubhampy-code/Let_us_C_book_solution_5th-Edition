distance_between_city = input("The distance between two cities (in km.):")
dis = float(distance_between_city)
in_meter = dis*1000
in_feet = dis*3280.84
in_inches = dis*39370.1
in_centimeter = dis*100000
print("The distance between two cities (in meter):" + str(in_meter))
print("The distance between two cities (in feet):"+ str(in_feet))
print("The distance between two cities (in inches):" + str(in_inches))
print("The distance between two cities (in centimeter):" + str(in_centimeter))


"""The distance between two cities (in km.) is input through the
keyboard. Write a program to convert and print this distance
in meters, feet, inches and centimeters. """