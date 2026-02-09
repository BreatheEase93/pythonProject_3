import json
from pathlib import Path
from typing import List, Optional, Tuple

from classes.category import Category
from classes.product import Product


def read_json(file_path: Optional[str] = None) -> Tuple[List[Category], List[Product]]:
    """Функция записи class из json файла"""
    if file_path is None:
        current_dir = Path(__file__).parent
        file_path = str(current_dir / "data" / "products.json")

    json_path = Path(file_path)

    if not json_path.exists():
        print(f"Файл не найден: {json_path}")
        return [], []


    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Ошибка JSON: {e}")
        return [], []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return [], []
    categories: List[Category] = []
    all_products: List[Product] = []

    for category_data in data:
        category_products: List[Product] = []
        for product_data in category_data.get("products", []):
            product = Product(
                name=product_data["name"],
                description=product_data.get("description", ""),
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            category_products.append(product)
            all_products.append(product)
        category = Category(
            name=category_data["name"],
            description=category_data.get("description", ""),
            products=category_products,
        )
        categories.append(category)

    return categories, all_products
