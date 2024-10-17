color_list = ["red", "orange", "yellow", "green", "blue"]

for color in color_list:
    print(color)

print("--------------------")

for index, color in enumerate(color_list):
    if index > 3:
        break
    else :
        print(index, color)