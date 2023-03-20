from collections import Counter

PER_BOOK = 800.00
PER_GROUP = {
    1: 1 * PER_BOOK * 1.00,
    2: 2 * PER_BOOK * 0.95,
    3: 3 * PER_BOOK * 0.90,
    4: 4 * PER_BOOK * 0.80,
    5: 5 * PER_BOOK * 0.75,
}


def _total(basket):
    basket_counts = Counter(basket)
    basket_set = set(basket)
    group_price = sum(PER_BOOK * (1 - (i-1)*0.05) * min(basket_counts[b], i) for i in range(2, 6) for b in basket_set)
    single_price = len(basket) * PER_BOOK
    return min(group_price, single_price)


def total(basket):
    if not basket:
        return 0
    return _total(sorted(basket))