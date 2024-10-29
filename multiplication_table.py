def get_multiplication_table_inputs():
    while True:
        base_number = (input("Enter a number for your multiplication table: "))
        maximum_product = (input("Enter the highest factor in the table: "))
        if base_number.isdigit() and maximum_product.isdigit():
            if int(base_number) <= int(maximum_product):
                return int(base_number), int(maximum_product)
            else:
                print("ERROR: Base number must be less than or equal to highest factor.")
        else: 
            print("ERROR: Please enter integers only.")


number, max_factor = get_multiplication_table_inputs()

for i in range(0, (int(max_factor / number) + 1)):
    print(f"{number} x {i} = {i * number}")        
