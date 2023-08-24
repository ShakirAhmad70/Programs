stores = {
    "medical_store": {
        "name": "MediCare",
        "items": ["bandages", "painkillers", "antibiotics", "thermometer"],
    },
    "general_store": {
        "name": "QuickMart",
        "items": ["toothpaste", "snacks", "cleaning supplies", "batteries"],
    },
    "clothes_store": {
        "name": "FashionFusion",
        "items": ["t-shirts", "jeans", "dresses", "shoes", "accessories"],
    },
    "electronics_store": {
        "name": "TechWorld",
        "items": ["laptops", "smartphones", "headphones", "televisions"],
    },
    "bookstore": {
        "name": "Book Haven",
        "items": ["novels", "self-help books", "children's books", "magazines"],
    },
    "stationery_store": {
        "name": "Paper Paradise",
        "items": ["notebooks", "pens", "sticky notes", "scissors", "glue"],
    },
    "home_decor_store": {
        "name": "Dreamy Decor",
        "items": ["candles", "vases", "wall art", "throw pillows", "rugs"],
    },
    "pet_store": {
        "name": "Paws & Claws",
        "items": ["dog food", "cat litter", "pet toys", "fish tank"],
    },
    "sporting_goods_store": {
        "name": "Active Outdoors",
        "items": ["football", "basketball", "tennis racket", "bicycle", "yoga mat"],
    },
    "jewelry_store": {
        "name": "Glamour Gems",
        "items": ["rings", "necklaces", "earrings", "bracelets", "watches"],
    },
    "music_store": {
        "name": "Melody Mart",
        "items": ["guitar", "piano", "drums", "microphone", "sheet music"],
    },
    "hardware_store": {
        "name": "Tool Time",
        "items": ["screwdriver", "hammer", "paint brushes", "power drill", "measuring tape"],
    },
}

def filter_items(store_name, keywords):
    if store_name not in stores:
        return []

    store = stores[store_name]
    filtered_items = [item for item in store["items"] if any(keyword.lower() in item.lower() for keyword in keywords)]
    return filtered_items

# Example usage
filters = [
    {"store_name": "medical_store", "keywords": ["bandages", "painkillers"]},
    {"store_name": "clothes_store", "keywords": ["jeans", "shoes"]},
    {"store_name": "electronics_store", "keywords": ["laptops", "headphones"]},
]

for filter_data in filters:
    store_name = filter_data["store_name"]
    keywords = filter_data["keywords"]

    filtered_items = filter_items(store_name, keywords)

    if filtered_items:
        print(f"Items matching any of the keywords in {stores[store_name]['name']}:")
        for item in filtered_items:
            print(item)
        print()  # Add a new line between store results
    else:
        print(f"No items matching the keywords found in {stores[store_name]['name']}.")
        print()  # Add a new line between store results
