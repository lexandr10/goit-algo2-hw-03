import csv
import random


def generate_csv(filename='generated_items_data.csv', num_items=10000):
    categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Toys']

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Category', 'Price'])  # Header

        for i in range(1, num_items + 1):
            item_id = i
            name = f"Item_{i}"
            category = random.choice(categories)
            price = round(random.uniform(5.0, 500.0), 2)
            writer.writerow([item_id, name, category, price])

    print(f"✅ Файл '{filename}' успішно створено з {num_items} товарами.")


# Запускаємо генерацію
generate_csv()
