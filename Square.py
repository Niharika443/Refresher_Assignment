import pandas as pd
a = [int(input("Enter the number:")) for i in range(5)]
ser_a = pd.Series(a)
print("Power of the numbers:",ser_a*ser_a)