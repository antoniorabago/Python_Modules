def ft_count_harvest_recursive() -> None:
    def helper(day: int, days: int) -> None:
        if (day > days):
            return
        print(f"Day {day}")
        helper(day + 1, days)
    day_one = 1
    days = int(input("Days until harvest: "))
    helper(day_one, days)
    print("Harvest time!")
