#hola mundo
# parrot_list = ["non pinin'", "no more", "a stiff", "bereft of live"]
#
# parrot_list.append("A Norwegian Blue")
#
# for state in parrot_list:
#     print("This parrot is " + state)
#
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# numbers_in_order = sorted(numbers)
#
# print(numbers_in_order)
#
# if numbers == numbers_in_order:
#     print("The lists are equal")
# else:
#     print("The lists are not equal")
#
# if numbers_in_order == sorted(numbers):
#     print("The lists are not equal")
# menu = []
# menu.append(["egg","spam","bacon"])
# menu.append(["egg","sausage","bacon"])
# menu.append(["egg","spam"])
# menu.append(["egg","bacon","spam"])
# menu.append(["egg","bacon","sausage","spam"])
# menu.append(["spam","bacon","sausage","spam"])
# menu.append(["spam","egg","spam","spam","bacon","spam"])
# menu.append(["spam","egg","sausage","spam"])
#
# for meal in menu:
#     if not "spam" in meal:
#         for plato in meal:
#             print(plato)

# items = ["lukyan","katja","daniel","the new one"]
# # print len(items)
# iterator = iter(items)
# for i in range(len(items)):
#     print(next(iterator))
imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

a, b, c, d = imelda
print(a)
print(b)
print(c)
print(d)

for tracks in d:
    #id, song = tracks
    print('\t', tracks)
