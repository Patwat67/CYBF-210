stock: dict = {"TwoBySixLumberBoards": 40,"Nails": 100,"Sheetrock": 30,"WallBeigePaint": 10,"CeilingWhitePaint": 15,"Screws": 3000,"Level": 10,"Hammer": 15,"Drill": 8,"Sandpaper": 200,"Spackle": 25}

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

def compute_bill(hardware:list):
    total:float = 0.00
    for item in hardware:
        total += price.get(item, 0)
    return total

def compute_bill_take_two(hardware:list):
    total:float = 0.00
    for item in hardware:
        if stock.get(item, 0) > 0:
            total += price.get(item, 0)
            stock[item] -= 1
    return total

tools = ["Nails", "Drill", "Sheetrock"]
print(f"Tools: {tools}\n"
      f"compute_bill total: ${compute_bill(tools):.2f}\n"
      f"compute_bill_take_two total: ${compute_bill_take_two(tools):.2f}")