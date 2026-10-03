#Author: Sebastian Medina
#I have decided to exceed the requirements by adding a Return by Date feature (as one of the suggested features in the Project Instructions)

import csv
from datetime import datetime, timedelta


def main():
    try:
        products_dict = read_dictionary("products.csv", 0)
        today_date = datetime.now()
        future_date = today_date + timedelta(days=30)
        return_by_date = future_date.replace(hour=21, minute=0, second=0)
        total_items = 0 
        subtotal = 0.0
        print("Inkom Emporium")

        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            print("Requested Items:")
            for row in reader:
                product_id = row[0]
                quantity = int(row[1])
                product_info = products_dict[product_id]
                name = product_info[1]
                price = float(product_info[2])
                total_items += quantity
                subtotal += quantity * price

                print(f"{name}: {quantity} @ {price}")

        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax
        
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print("Thank you for shopping at the Inkom Emporium.")
        print(f"{today_date:%a %b %d %H:%M:%S %Y}")
        print(f"Return by: {return_by_date:%a %b %d %I:%M %p %Y}")

    except FileNotFoundError as a:
        print("Error: missing file")
        print(a)
    except PermissionError as e:
        print("Error: permission denied")
        print(e)
    except KeyError as i:
        print("Error: unknown product ID in the request.csv file")
        print(i)

def read_dictionary(filename, key_column_index):
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary

if __name__ == "__main__":
    main()