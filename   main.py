# --- Shopping Data Analysis ---

purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

# --- 1. Total Revenue ---
def total_revenue(purchases):
    return sum(p["price"] * p["quantity"] for p in purchases)

# --- 2. Items by Category ---
def items_by_category(purchases):
    categories = {}
    for p in purchases:
        categories.setdefault(p["category"], set()).add(p["item"])
    return categories

# --- 3. Expensive Purchases ---
def expensive_purchases(purchases, min_price):
    return [p for p in purchases if p["price"] >= min_price]

# --- 4. Average Price by Category ---
def average_price_by_category(purchases):
    category_prices = {}
    for p in purchases:
        category_prices.setdefault(p["category"], []).append(p["price"])
    return {
        cat: sum(prices) / len(prices)
        for cat, prices in category_prices.items()
    }

# --- 5. Most Frequent Category ---
def most_frequent_category(purchases):
    category_counts = {}
    for p in purchases:
        category_counts[p["category"]] = category_counts.get(p["category"], 0) + p["quantity"]
    return max(category_counts, key=category_counts.get)

# --- Usage Example ---
min_price = 1.0
expensive = expensive_purchases(purchases, min_price)

# --- Output ---
print("Общая выручка:", total_revenue(purchases))
print("Товары по категориям:", items_by_category(purchases))
print(f"Покупки дороже {min_price}:", expensive)
print("Средняя цена по категориям:", average_price_by_category(purchases))
print("Категория с наибольшим количеством проданных товаров:", most_frequent_category(purchases))