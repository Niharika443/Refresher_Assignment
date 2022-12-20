import pandas as pd
n1 = [int(input("Enter values of n1: ")) for i in range(4)]
n2 = [int(input("Enter values of n2: ")) for i in range(4)]
ser_n1 = pd.Series(n1)
ser_n2 = pd.Series(n2)
print("Pandas series of n1 are:",ser_n1)
print("Pandas series of n2 are:",ser_n2)
print("Addition of numbers in two pandas series is",ser_n1+ser_n2)
print("Subtraction of numbers in two pandas series is",ser_n1-ser_n2)
print("Multiplication of numbers in two pandas series is",ser_n1*ser_n2) 
print("Division of numbers in two pandas series is",ser_n1/ser_n2)
print("Remainder of numbers in two pandas series is",ser_n1%ser_n2)