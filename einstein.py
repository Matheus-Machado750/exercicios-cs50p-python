def einstein(m):

    c = 300000000
    e = m * (c * c)

    return e

m = int(input("Diga a massa em Kg :"))

result = einstein(m)

print(result)
