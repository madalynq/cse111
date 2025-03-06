item_num = int(input("Enter the number of items: "))
box_num = int(input("Enter the number of items per box: "))

import math
total = math.ceil(item_num / box_num)
print(f"For {item_num} items, packing {box_num} items in each box, you will need {total} boxes.")