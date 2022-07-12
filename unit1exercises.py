# Unit 1: Exercise 2
# Practice using the Python interpreter as a calculator:
#
# 1. The volume of a sphere with radius r is 4/3 π r3. What is the volume of a sphere with radius 5?
# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

# 1. Exercise

from math import pi           # known from the MIMO app
r = 5
volume = 4/3 * pi * r**3
print("The volume of the Sphere is:", volume)


# 2. Exercise

cover_price = 24.95
discount = 0.40
shipping_cost = 3
each_other = 0.75
order = 60

discounted_price = cover_price - (cover_price * discount)
total_order = discounted_price * order
print("The discounted cover price is:", total_order)

total_shipping = shipping_cost + (each_other * (order - 1))
print("The total shipping cost is:", total_shipping)

print("The total wholesale for 60 copies is:", total_order + total_shipping)


# 3. Exercise


start_time = (6 * 60 + 52) * 60    # start of running at 6:52 am
one_mile_pace = 8 * 60 + 15
three_miles_pace = 7 * 60 + 12

total_running = one_mile_pace + (three_miles_pace * 3) + one_mile_pace
total_time = (start_time + total_running) / (60*60)     # running time in hours
total_time_int = int(total_time)

total_time_min = (total_time - total_time_int) * 60
total_time_min_int = int(total_time_min)

print("Breakfast will be at:", total_time_int, ":", total_time_min_int)

