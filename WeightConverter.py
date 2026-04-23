#Python Weight Converter lbs to kg or kg to lbs

weight = float(input("Please enter the weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

while unit.upper() not in ["K", "L"]:
    print(f"{unit} was not recognized. \nPlease try again.")
    unit = input("Kilograms or Pounds? (K or L): ")


if unit.upper() == "K":
    weight = weight * 2.20462
    unit = "lbs"
elif unit.upper() == "L":
    weight = weight *  0.453952
    unit = "kgs"

print(f"The weight is: {round(weight,2)} {unit}")