def nested_loops(idx, output_number):
    if idx >= len(output_number):
        print(*output_number, sep=" ")
        return
    for num in range(1, loops + 1):
        output_number[idx] = num
        nested_loops(idx + 1, output_number)


loops = int(input())
output_number = [1] * loops

nested_loops(0, output_number)
