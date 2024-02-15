from bookapidao import getallbooks

books = getallbooks()
total = 0
count = 0
for book in books:
    total += book["Price"]
    count += 1


print("The average price of", count, "books is", "€",total/count)