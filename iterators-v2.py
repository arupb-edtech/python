students = ["Alice", "Bob", "Charlie"]

iterator = iter(students)
print(next(iterator))  # Output: Alice
print(next(iterator))  # Output: Bob
print(next(iterator))  # Output: Charlie
print(next(iterator))  # Raises StopIteration
