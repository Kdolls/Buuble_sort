# import pygame


# pygame Header
# pygame.init()
#
# color = (255, 000, 000)
# rect_color = (255, 0, 0)
#
# # CREATING CANVAS
# canvas = pygame.display.set_mode((500, 500))

# TITLE OF CANVAS
# pygame.display.set_caption("Show Image")
#
# # image = pygame.image.load("Screenshot.png")
# exit = False
#
# while not exit:
#     canvas.fill(color)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit = True
#
#     pygame.draw.rect(canvas, rect_color,
#                      pygame.Rect(30, 30, 60, 60))
#     pygame.display.update()

# ----------------------------------------------end Header


# def bubbleSort(array):
#     # loop through each element of array
#     for i in range(len(array)):
#
#         # keep track of swapping
#         swapped = False
#
#         # loop to compare array elements
#         for j in range(0, len(array) - i - 1):
#
#             # compare two adjacent elements
#             # change > to < to sort in descending order
#             if array[j] > array[j + 1]:
#                 # swapping occurs if elements
#                 # are not in the intended order
#                 temp = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = temp
#
#                 swapped = True
#
#         # no swapping means the array is already sorted
#         # so no need for further comparison
#         if not swapped:
#             break
#
#
# my_list = [12, 34, 5, 8, 9, 43, 56, 87, 3, 1, 65, 8]
# print('list before: ', my_list)
# bubbleSort(my_list)
# print('list after: ',my_list)


#
# # pseudocode
def bubble_sort(lis):
    n = len(lis)

    for x in range(n):
        for y in range(0, n - x - 1 - 1):
            swapped = False

        #   different form for swap function
            # temp = lis[y]
            # lis[y] = lis[y + 1]
            # lis[y + 1] = temp

            # the swap function
            if lis[y] > lis[y + 1]:
                lis[y], lis[y + 1] = lis[y + 1], lis[y]

            swapped = True
            if not swapped:
                break
        # print(bubble_sort(lis))


my_list = [12, 34, 5, 8, 9, 43, 56, 87, 3, 1, 65, 8]

print('my list before: ', my_list)

bubble_sort(my_list)
print('my list after: ', my_list)
