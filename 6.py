lot_to_gram = 13.3
pount_to_lot = 32
talent_to_pound = 20
talent = int(input("Enter the number of talents: "))
pound = int(input("Enter the number of pounds: "))
lot = int(input("Enter the number of lots: "))
total_pound = talent * talent_to_pound
total_pound += pound
total_lot = total_pound * pount_to_lot
total_gram = total_lot * lot_to_gram
kilograms = int(lot_to_gram // 1000)
grams = total_gram % 1000
print(f"The total mass is {kilograms} kilograms and {grams:.1f} grams.")