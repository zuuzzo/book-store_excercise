def total(basket):
    book_counts = [0] * 5
    for book in basket:
        book_counts[book - 1] += 1

    num_books = sum(book_counts)
    unique_books = sum(1 for count in book_counts if count > 0)

    prices = [800, 1520, 2160, 2560, 3000]

    total_cost = 0
    while num_books > 0:
        # Determine the maximum number of different books that can be purchased in this iteration
        max_books = min(max(book_counts), 4, unique_books)

        # Calculate the cost of purchasing this many books
        group_cost = prices[max_books - 1] * max_books

        # Subtract the purchased books from book_counts and num_books
        for i in range(len(book_counts)):
            if book_counts[i] >= max_books:
                book_counts[i] -= max_books
                num_books -= max_books
            else:
                num_books -= book_counts[i]
                book_counts[i] = 0
            if book_counts[i] > 0:
                unique_books += 1

        # Add the cost of this group of books to the total cost
        total_cost += group_cost

    return total_cost