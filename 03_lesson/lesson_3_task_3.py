from Address import Address
from Mailing import Mailing

to_address = Address("123456", "Москва",
                     "Тверская", "10", "5")
from_address = Address("654321", "Санкт-Петербург",
                       "Невский проспект", "25", "12")

mailing = Mailing(to_address, from_address, 350, "TRACK12345678")

print(f"Отправление {mailing.track} из "
      f"{mailing.from_address.index}, "
      f"{mailing.from_address.city}, "
      f"{mailing.from_address.street}, "
      f"{mailing.from_address.house} - "
      f"{mailing.from_address.flat} "
      f"в {mailing.to_address.index}, "
      f"{mailing.to_address.city}, "
      f"{mailing.to_address.street}, "
      f"{mailing.to_address.house} - "
      f"{mailing.to_address.flat}. Стоимость "
      f"{mailing.cost} рублей.")
