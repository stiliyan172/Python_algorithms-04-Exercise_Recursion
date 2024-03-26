# nums = [int(x) for x in input().split()]
# reversed_list = nums[::-1]
# print(*reversed_list, sep=" ")

# print(*[int(x) for x in input().split()][::-1], sep=" ") # Ugly! Don't try this at home

elements = input().split()


def reverse_array(idx, elements):
    if idx == len(elements) // 2:
        return
    swap_idx = len(elements) - 1 - idx
    elements[idx], elements[swap_idx] = elements[swap_idx], elements[idx]
    reverse_array(idx + 1, elements)


reverse_array(0, elements)

print(*elements)
