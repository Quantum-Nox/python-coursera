largest = None
smallest = None
while True:
    try:
        num = raw_input("Enter a number: ")
        if num == 'done':
            break
        n = int(num)
        print("prima degli if", largest, smallest)
        if largest == None:
            largest = n
        if smallest == None:
            smallest = n
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n
        print("dopo if",largest, smallest)
    except:
        print("Invalid input")
        print("from except",largest, smallest)

print("Maximum is", largest)
print("Minimum is", smallest)
