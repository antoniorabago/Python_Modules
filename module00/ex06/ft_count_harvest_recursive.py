def ft_count_harvest_recursive():
    def helper(day: int):
        print(f"Day {day}")
        helper(day - 1)
    days = int(input("Days until harvest: "))
    helper(days)
    print("Harvest time!")
