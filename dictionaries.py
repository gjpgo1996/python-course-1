product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

person = {
    "first_name": "Ryan",
    "last_name": "Ray"
}

# print(type(product))
# print(dir(product))

# print(person.keys())
# print(person.items())
print(person.values())
person.clear()
#del person
print(person)

products = [
    {"name": 'book', "price": 10.99},
    {"name": 'laptop', "price": 1000}
]

print(products)