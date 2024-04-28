# Complement Angle and Supplement Angle Calculator

import math

def main():
    
    # Take Degree and Inch information from the user
    
    inputDegree = float(input("How many degrees were you given? (i.e. 127 for 127°)"))
    print(" ")
    inputInch = float(input("How many inches were you given? (i.e. 20 for 20')"))
    
    # Conversion math given the user's input
    
    complementDegree = 89 - inputInch
    supplementDegree = 179 - inputDegree
    inches = 60 - inputInch
    
    # Print the results of the conversion/calculation
    
    print(" ")
    print("The complement degree is " + str(complementDegree) + ".")
    print("The supplement degree is " + str(supplementDegree) + ".")
    print("The new inches amount is " + str(inches) + ".")
    
main()
