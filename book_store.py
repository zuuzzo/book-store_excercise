def total(basket):
    BOOK_PRICE = 800
    DISCOUNT_RATES = {1: 0, 2: 0.05, 3: 0.10, 4: 0.20, 5: 0.25}
    costs = {}
    for book in basket:
        if book not in costs:
            costs[book] = 0
        costs[book] += 1

    total_cost = 0
    while costs:
        unique_books = len(costs)
        group_cost = unique_books * BOOK_PRICE * (1 - DISCOUNT_RATES[unique_books])
        total_cost += group_cost

        for book in list(costs.keys()):
            costs[book] -= 1
            if costs[book] == 0:
                del costs[book]

    return total_cost