from pymongo import MongoClient
from datetime import datetime

# Sample data
purchase_data = [
    {
        "name": "John Smith",
        "place": "New York City",
        "mode_of_payment": "Credit Card",
        "amount": 299.99,
        "item_bought": "Wireless Headphones",
        "timestamp": datetime.now()
    },
    {
        "name": "Emma Wilson",
        "place": "Los Angeles",
        "mode_of_payment": "PayPal",
        "amount": 1299.99,
        "item_bought": "Laptop",
        "timestamp": datetime.now()
    },
    {
        "name": "Michael Chen",
        "place": "San Francisco",
        "mode_of_payment": "Debit Card",
        "amount": 89.99,
        "item_bought": "Fitness Tracker",
        "timestamp": datetime.now()
    },
    {
        "name": "Sarah Johnson",
        "place": "Chicago",
        "mode_of_payment": "Cash",
        "amount": 45.50,
        "item_bought": "Books",
        "timestamp": datetime.now()
    },
    {
        "name": "David Brown",
        "place": "Houston",
        "mode_of_payment": "Apple Pay",
        "amount": 799.99,
        "item_bought": "Smartphone",
        "timestamp": datetime.now()
    },
    {
        "name": "Lisa Garcia",
        "place": "Miami",
        "mode_of_payment": "Credit Card",
        "amount": 150.00,
        "item_bought": "Running Shoes",
        "timestamp": datetime.now()
    },
    {
        "name": "James Wilson",
        "place": "Seattle",
        "mode_of_payment": "Google Pay",
        "amount": 599.99,
        "item_bought": "Gaming Console",
        "timestamp": datetime.now()
    },
    {
        "name": "Maria Rodriguez",
        "place": "Phoenix",
        "mode_of_payment": "PayPal",
        "amount": 75.99,
        "item_bought": "Yoga Mat",
        "timestamp": datetime.now()
    },
    {
        "name": "Robert Taylor",
        "place": "Boston",
        "mode_of_payment": "Credit Card",
        "amount": 2499.99,
        "item_bought": "4K TV",
        "timestamp": datetime.now()
    },
    {
        "name": "Jennifer Lee",
        "place": "San Diego",
        "mode_of_payment": "Debit Card",
        "amount": 129.99,
        "item_bought": "Coffee Maker",
        "timestamp": datetime.now()
    },
    {
        "name": "William Anderson",
        "place": "Denver",
        "mode_of_payment": "Cash",
        "amount": 35.00,
        "item_bought": "Pizza",
        "timestamp": datetime.now()
    },
    {
        "name": "Patricia Martinez",
        "place": "Austin",
        "mode_of_payment": "Venmo",
        "amount": 249.99,
        "item_bought": "Smartwatch",
        "timestamp": datetime.now()
    },
    {
        "name": "Thomas Wright",
        "place": "Portland",
        "mode_of_payment": "Credit Card",
        "amount": 899.99,
        "item_bought": "iPad",
        "timestamp": datetime.now()
    },
    {
        "name": "Elizabeth White",
        "place": "Atlanta",
        "mode_of_payment": "Apple Pay",
        "amount": 65.99,
        "item_bought": "Bluetooth Speaker",
        "timestamp": datetime.now()
    },
    {
        "name": "Kevin Thompson",
        "place": "Las Vegas",
        "mode_of_payment": "PayPal",
        "amount": 199.99,
        "item_bought": "Air Purifier",
        "timestamp": datetime.now()
    },
    {
        "name": "Nancy Davis",
        "place": "Nashville",
        "mode_of_payment": "Credit Card",
        "amount": 450.00,
        "item_bought": "Concert Tickets",
        "timestamp": datetime.now()
    },
    {
        "name": "Christopher Moore",
        "place": "Philadelphia",
        "mode_of_payment": "Google Pay",
        "amount": 1799.99,
        "item_bought": "Gaming PC",
        "timestamp": datetime.now()
    },
    {
        "name": "Amanda Miller",
        "place": "Minneapolis",
        "mode_of_payment": "Debit Card",
        "amount": 79.99,
        "item_bought": "Office Chair",
        "timestamp": datetime.now()
    },
    {
        "name": "Daniel Kim",
        "place": "Washington DC",
        "mode_of_payment": "Cash",
        "amount": 25.99,
        "item_bought": "Phone Case",
        "timestamp": datetime.now()
    },
    {
        "name": "Michelle Turner",
        "place": "Orlando",
        "mode_of_payment": "Venmo",
        "amount": 349.99,
        "item_bought": "Drone",
        "timestamp": datetime.now()
    }
]


# MongoDB connection and insertion code
def insert_sample_data():
    # Replace with your MongoDB connection string
    client = MongoClient('mongodb://localhost:27017/')
    db = client['BARBARIK']
    collection = db['CUSTOMERS_DETAILS']

    # Insert the data
    result = collection.insert_many(purchase_data)

    print(f"Inserted {len(result.inserted_ids)} documents")
    return result.inserted_ids


if __name__ == "__main__":
    insert_sample_data()