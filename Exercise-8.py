stock: dict = {
    "TwoBySixLumberBoards": 120,
    "Nails": 5000,
    "Sheetrock": 50,
    "WallBeigePaint": 20,
    "CeilingWhitePaint": 15,
    "Screws": 3000,
    "Level": 10,
    "Hammer": 15,
    "Drill": 8,
    "Sandpaper": 200,
    "Spackle": 25
}

price: dict = {
    "TwoBySixLumberBoards": 3.75,
    "Nails": 0.01,
    "Sheetrock": 13.50,
    "WallBeigePaint": 29.99,
    "CeilingWhitePaint": 27.49,
    "Screws": 0.02,
    "Level": 14.99,
    "Hammer": 18.99,
    "Drill": 59.99,
    "Sandpaper": 0.25,
    "Spackle": 8.49
}

available_hardware:list = ["TwoBySixLumberBoards", "Nails", "Sheetrock", "WallBeigePaint", "CeilingWhitePaint", "Screws", "Level", "Hammer", "Drill", "Sandpaper", "Spackle"]

def compute_bill(hardware:list):
    total:float = 0.00 # initialize the total
    for item in hardware:
        total += price.get(item, 0) # iterate over hardware and add price to total
    return total

def compute_bill_take_two(hardware:list):
    total:float = 0.00
    for item in hardware:
        if stock.get(item, 0) > 0:
            total += price.get(item, 0)
            stock[item] -= 1 # Decrease stock by one
    return total


def test_compute_bill_functions():
    test_items = ["Nails", "Hammer", "Drill"]

    # Expected total from compute_bill
    expected_total = price["Nails"] + price["Hammer"] + price["Drill"]

    # Test compute_bill
    total1 = compute_bill(test_items)
    assert abs(total1 - expected_total) < 1e-6, f"compute_bill failed: expected {expected_total}, got {total1}"
    print(f"compute_bill\n"
          f"Hardware: {test_items}\n "
          f"Total: {round(total1, 2)}\n")

    # Copy current stock to measure stock decrease
    original_stock = stock.copy()

    # Test compute_bill_take_two
    total2 = compute_bill_take_two(test_items)
    assert abs(total2 - expected_total) < 1e-6, f"compute_bill_take_two failed: expected {expected_total}, got {total2}"
    print(f"compute_bill_take_two\n"
          f"Hardware: {test_items}\n"
          f"Original stock: {', '.join(f'{item}: {original_stock.get(item)}' for item in test_items)}\n"
          f"Updated stock: {', '.join(f'{item}: {stock.get(item)}' for item in test_items)}\n"
          f"Total: {round(total2, 2)}\n")

    # Validate stock decrease
    for item in test_items:
        assert stock[item] == original_stock[item] - 1, f"Stock not decremented for {item}"

# Run the test
if __name__ == "__main__":
    test_compute_bill_functions()
