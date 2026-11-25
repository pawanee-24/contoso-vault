DAYS_IN_WEEK: int = 7

day = int(input("Enter Day: ")) #6
days_to_wait = int(input("Enter Days to wait: ")) #3

delivery_day: int = day + days_to_wait # 9

if delivery_day > DAYS_IN_WEEK:
    delivery_day = delivery_day - DAYS_IN_WEEK
    print("Delivery Day: ", delivery_day)
else:
    print("Delivery Day: ", delivery_day)

assert 1 <= delivery_day <= 7, "invalid delivery day"