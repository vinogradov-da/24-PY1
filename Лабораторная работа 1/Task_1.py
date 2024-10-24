numbers = [2, -93, -2, 8, None , -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO заменить значение пропущенного элемента средним арифметическим
summa_chisel = sum(filter(None,numbers))
quantity_chisel = len(numbers)
averege = summa_chisel / quantity_chisel
numbers[4] = averege
print("Измененный список:", numbers)
