import csv
import random
import timeit
from BTrees._OOBTree import OOBTree

CSV_FILE = "generated_items_data.csv"

oobtree = OOBTree()
dict_store = {}

def add_item_to_tree(tree, item_id, item_data):
    tree[item_id] = item_data

def add_item_to_dict(store, item_id, item_data):
    store[item_id] = item_data


def range_query_tree(tree, min_price, max_price):
    return [v for v in tree.values() if min_price <= float(v["Price"]) <= max_price]

def range_query_dict(store, min_price, max_price):
    return [v for v in store.values() if min_price <= float(v["Price"]) <= max_price]

with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        item_id = int(row["ID"])
        item_data = {
            "Name": row["Name"],
            "Category": row["Category"],
            "Price": row["Price"],
        }
        add_item_to_tree(oobtree, item_id, item_data)
        add_item_to_dict(dict_store, item_id, item_data)

min_price = 10
max_price = 100

def test_range_tree():
    range_query_tree(oobtree, min_price, max_price)

def test_range_dict():
    range_query_dict(dict_store, min_price, max_price)

# Вимірювання часу
TIME_REPEAT = 100

time_tree = timeit.timeit(test_range_tree, number=TIME_REPEAT)
time_dict = timeit.timeit(test_range_dict, number=TIME_REPEAT)

# Виведення результатів
print(f"Total range_query time for OOBTree: {time_tree:.6f} seconds")
print(f"Total range_query time for Dict: {time_dict:.6f} seconds")
