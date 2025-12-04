
# Portada:
#   Name: Alejandro De Leon Fonseca                          Matriculation: 2530020
#                                          Group: IM 1-3
#
# Executive summary:
"""
This program implements a simple in-memory CRUD (Create, Read, Update, Delete)
manager for items (inventory-like records). Each item has id, name, price and
quantity. The implementation uses a dict mapping item_id -> item_dict for
O(1) lookups and clear semantics.
Functions are used to encapsulate each operation: create_item, read_item,
update_item, delete_item, list_items. Input validation is performed before
calling operations and messages follow the required English outputs.
"""

# Problem: In-memory CRUD manager with functions

# Description:
"""
Program that implements a CRUD (Create, Read, Update, Delete) simple manager
using a dictionary as the primary data structure. The program exposes a
text menu for interaction and uses functions to perform each operation.
"""
# Inputs:
"""
User menu options (int as string acceptable)
For CREATE/UPDATE: item_id (string), name (string), price (float), quantity (int)
For READ/DELETE: item_id (string)
"""
# Outputs:
#   - "Item created"
#   - "Item updated"
#   - "Item deleted"
#   - "Item not found"
#   - "Items list:" (followed by readable list)
#   - "Error: invalid input"

# Validations:
"""
- menu option must be valid (0..5)
- item_id must not be empty
- price must be convertible to float and >= 0.0
- quantity must be convertible to int and >= 0
- creating an item with an existing id is not allowed
- reading/updating/deleting a non-existing id yields "Item not found"
"""
# Test cases:
"""
1) Normal:
   - Create item id="p1", name="Pen", price=1.5, quantity=10 -> "Item created"
   - Read "p1" -> prints item details
   - Update "p1" price=2.0 quantity=5 -> "Item updated"
   - Delete "p1" -> "Item deleted"
 2) Border:
   - Create item with quantity = 0 (allowed) -> "Item created"
 3) Error:
   - Create with empty id or non-numeric price -> "Error: invalid input"
"""

# Optional diagram/table (text):
# "Flowchart: Start -> show menu -> read option -> validate -> call function ->
#  show result -> repeat until option 0 -> End"


# Data structure decision:
# - I choose OPTION A: a dict where key = item_id (string) and value = dict with
#   fields {"name": str, "price": float, "quantity": int}.
# - Reason: fast lookups, simple check for existence, easy updates and deletions.


# Constants
EXIT_OPTION = 0
CREATE_OPTION = 1
READ_OPTION = 2
UPDATE_OPTION = 3
DELETE_OPTION = 4
LIST_OPTION = 5
MAX_ITEMS = 1000  # optional safety limit (not enforced strictly)


# CRUD functions

def create_item(data_store, item_id, name, price, quantity):
    """
    Create a new item in data_store (dict).
    Returns True on success, False if id exists.
    Assumes inputs already validated by caller.
    """
    if item_id in data_store:
        return False  # id already exists
    data_store[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True


def read_item(data_store, item_id):
    """
    Return the item dict if found, otherwise None.
    """
    return data_store.get(item_id)


def update_item(data_store, item_id, new_name=None, new_price=None, new_quantity=None):
    """
    Update item fields if item exists.
    Returns True if updated, False if item not found.
    Only non-None parameters will be updated.
    """
    item = data_store.get(item_id)
    if item is None:
        return False
    if new_name is not None:
        item["name"] = new_name
    if new_price is not None:
        item["price"] = new_price
    if new_quantity is not None:
        item["quantity"] = new_quantity
    return True


def delete_item(data_store, item_id):
    """
    Delete item by id. Returns True if deleted, False if not found.
    """
    if item_id in data_store:
        data_store.pop(item_id)
        return True
    return False


def list_items(data_store):
    """
    Print items in a readable format. Returns a list of item dicts for possible testing.
    """
    print("Items list:")
    items_out = []
    if not data_store:
        print("(no items)")
        return items_out
    for item_id, info in data_store.items():
        line = f"- id: {item_id}, name: {info['name']}, price: {info['price']}, quantity: {info['quantity']}"
        print(line)
        items_out.append({"id": item_id, **info})
    return items_out



# Input validation helpers

def validate_non_empty_string(value):
    if value is None:
        return False
    if isinstance(value, str) and value.strip() != "":
        return True
    return False


def parse_price(value_str):
    try:
        p = float(value_str)
    except (TypeError, ValueError):
        raise ValueError("invalid input")
    if p < 0.0:
        raise ValueError("invalid input")
    return p


def parse_quantity(value_str):
    try:
        q = int(value_str)
    except (TypeError, ValueError):
        raise ValueError("invalid input")
    if q < 0:
        raise ValueError("invalid input")
    return q


def parse_menu_option(value_str):
    try:
        opt = int(value_str)
    except (TypeError, ValueError):
        raise ValueError("invalid input")
    if opt not in {EXIT_OPTION, CREATE_OPTION, READ_OPTION, UPDATE_OPTION, DELETE_OPTION, LIST_OPTION}:
        raise ValueError("invalid input")
    return opt



# Main program (menu)

def show_menu():
    print()
    print("Menu:")
    print("1) Create item")
    print("2) Read item by id")
    print("3) Update item by id")
    print("4) Delete item by id")
    print("5) List all items")
    print("0) Exit")


def main():
    data_store = {}  # main dict: item_id -> {"name", "price", "quantity"}

    while True:
        show_menu()
        raw_option = input("Option: ").strip()
        try:
            option = parse_menu_option(raw_option)
        except ValueError:
            print("Error: invalid input")
            continue

        if option == EXIT_OPTION:
            # Exit
            break

        elif option == CREATE_OPTION:
            # CREATE
            item_id = input("id: ").strip()
            if not validate_non_empty_string(item_id):
                print("Error: invalid input")
                continue
            name = input("name: ").strip()
            if not validate_non_empty_string(name):
                print("Error: invalid input")
                continue
            price_str = input("price: ").strip()
            quantity_str = input("quantity: ").strip()
            try:
                price = parse_price(price_str)
                quantity = parse_quantity(quantity_str)
            except ValueError:
                print("Error: invalid input")
                continue

            # policy: do not allow duplicate ids
            success = create_item(data_store, item_id, name, price, quantity)
            if success:
                print("Item created")
            else:
                print("Error: invalid input")  # duplicate id treated as invalid per spec

        elif option == READ_OPTION:
            # READ
            item_id = input("id: ").strip()
            if not validate_non_empty_string(item_id):
                print("Error: invalid input")
                continue
            item = read_item(data_store, item_id)
            if item is None:
                print("Item not found")
            else:
                print(f"id: {item_id}, name: {item['name']}, price: {item['price']}, quantity: {item['quantity']}")

        elif option == UPDATE_OPTION:
            # UPDATE
            item_id = input("id: ").strip()
            if not validate_non_empty_string(item_id):
                print("Error: invalid input")
                continue
            # Check existence first
            if read_item(data_store, item_id) is None:
                print("Item not found")
                continue
            # For update, accept blank to mean "no change" for name; but numeric fields must be validated if provided
            new_name_raw = input("new name (leave blank to keep): ")
            new_name = None
            if new_name_raw is not None and new_name_raw.strip() != "":
                new_name = new_name_raw.strip()

            new_price_raw = input("new price (leave blank to keep): ").strip()
            new_price = None
            if new_price_raw != "":
                try:
                    new_price = parse_price(new_price_raw)
                except ValueError:
                    print("Error: invalid input")
                    continue

            new_quantity_raw = input("new quantity (leave blank to keep): ").strip()
            new_quantity = None
            if new_quantity_raw != "":
                try:
                    new_quantity = parse_quantity(new_quantity_raw)
                except ValueError:
                    print("Error: invalid input")
                    continue

            updated = update_item(data_store, item_id, new_name, new_price, new_quantity)
            if updated:
                print("Item updated")
            else:
                print("Item not found")  # should not happen because we checked earlier

        elif option == DELETE_OPTION:
            # DELETE
            item_id = input("id: ").strip()
            if not validate_non_empty_string(item_id):
                print("Error: invalid input")
                continue
            deleted = delete_item(data_store, item_id)
            if deleted:
                print("Item deleted")
            else:
                print("Item not found")

        elif option == LIST_OPTION:
            # LIST
            list_items(data_store)

        else:
            # defensive
            print("Error: invalid input")

    print("Goodbye.")


# Only run main when executed as script
if __name__ == "__main__":
    main()



# Conclusions:
"""
Using functions for each CRUD operation keeps the menu logic simple and
delegates validation and mutation to well-named routines.
A dict mapping id -> dict was chosen because it provides O(1) lookup for
read/update/delete, making the manager efficient and straightforward.
Input validation was a significant part of the work: parsing numeric types
and rejecting empty ids prevents inconsistent state.
This in-memory manager can be extended to persist data (e.g., JSON file or DB)
or to add more fields and business rules.
"""

# References:
# 1) Python documentation - Data structures: dict, list. https://docs.python.org/3/tutorial/datastructures.html
# 2) Python documentation - Defining functions. https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 3) Tutorials and examples on CRUD patterns in Python (various online resources)

