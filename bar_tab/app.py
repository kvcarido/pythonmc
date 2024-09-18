from pathlib import Path
import csv

def drink_order():
    order = []
    while True:
        drink = input("Drink name (or type 'f' to finish): ")
        if drink.lower() == 'f':
            break
        try:
            price = float(input(f"{drink} price: "))
            # add to order list as tuples
            order.append((drink, price))
        except ValueError:
            print("Invalid - please enter a number")
    return order

def get_totals(order):
    subtotal = sum(price for drink, price in order)
    tip = round(subtotal * 0.20, 2)
    grand_total = subtotal + tip
    # returns a tuple
    return subtotal, tip, grand_total

def write_check(table_num, order, subtotal, tip, grand_total):
    # create a file path using table number
    path = Path(__file__).parent / f"table_{table_num}.csv"

    # write order and totals to csv
    with path.open("w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Drink Name", "Price"])
        writer.writerows(order)
        writer.writerow(["Subtotal", subtotal])
        writer.writerow(["Tip", tip])
        writer.writerow(["Grand Total", grand_total])

        print(f"The bar tab has been saved to {path}")
    return

def main():
    # get table number from user
    while True:
        try:
            table_num = int(input("Table number: "))
            print(f"Starting a tab for Table {table_num}...")
            break
        except ValueError:
            print("Not a valid number")
            continue

    # get items from user (drink name and price)
    order = drink_order()
    
    if not order:
        print("No drinks added - exiting program.")
        return

    # calculate the totals (total, tip, grand_total)
    subtotal, tip, grand_total = get_totals(order)

    # create the csv
    write_check(table_num, order, subtotal, tip, grand_total)

if __name__ == '__main__':
    main()