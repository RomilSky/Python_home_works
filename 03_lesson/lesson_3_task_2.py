from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79123456789"),
    Smartphone("Samsung", "Galaxy S25", "+79234567890"),
    Smartphone("Xiaomi", "Mi 11", "+79345678901"),
    Smartphone("Oppo", "reno 13", "+79456789012"),
    Smartphone("Google", "Pixel 10", "+79567890123")
]

for phone in catalog:
    print(f"{phone.phone_brand} - {phone.phone_model}. "
          f"{phone.subscriber_number}")
