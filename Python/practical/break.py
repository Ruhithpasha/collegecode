# str = "ruhith"
# for i in "ruhith":
#     if i == "":
#         break
#     print(i)


# for letter in "python":
#     if letter == "h":
#         break
#     print("Current letter:", letter)


# for num in [1, 11, 9, 66, 4,89,]:
#     if num%2 ==0:
#         continue
#     print("Current number:", num)


for i in range(5):
    for j in range(5):
        if j == 3:
            break
    if i == 3:
        break
    print("i:", i, "j:", j)