def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    while (days > 0):
        print(f"Day {days}")
        days -= 1
    print("Harvest time!")
