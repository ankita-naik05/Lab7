temp_c = float(input("Enter temperature in °C: "))
if temp_c < 20:
    print("Cold")
elif 20 <= temp_c <= 30:
    print("Normal")
else:
    print("Hot")
temp_f = (temp_c * 9/5) + 32