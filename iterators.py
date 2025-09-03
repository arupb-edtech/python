# Iterators in Python

# An iterator is an object that contains a countable number of values`
# and can be iterated upon, meaning that you can traverse through all the values.
# Technically, an iterator is any object which implements the iterator protocol,
# which consist of the methods __iter__() and __next__().
# An object is called iterable if we can get an iterator from it.
# Most built-in containers in Python like: list, tuple, string etc. are iterables.
# They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator.
# Example of an iterator:
# Creating an iterable
my_tuple = ("apple", "banana", "cherry")
# Getting an iterator from the iterable
my_iter = iter(my_tuple)
# Iterating through the iterator using next()
print(next(my_iter))  # Output: apple
print(next(my_iter))  # Output: banana
print(next(my_iter))  # Output: cherry
# If we call next() again, it will raise a StopIteration exception
# print(next(my_iter))  # Uncommenting this line will raise StopIteration
# You can also use a for loop to iterate through an iterable
for item in my_tuple:
    print(item)
# Output:
# apple
# banana
# cherry
# This is because a for loop internally creates an iterator from the iterable
# and calls next() on it until it raises a StopIteration exception.
# Creating a custom iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
my_numbers = MyNumbers()
my_iter = iter(my_numbers)
for num in my_iter:
    print(num)
# Output:
# 1
# 2
# 3
# 4
# 5
# In this example, MyNumbers is a custom iterator that returns numbers from 1 to 5.
# The __iter__() method initializes the starting value and returns the iterator object itself.
# The __next__() method returns the next value and raises StopIteration when there are no more values to return.
# You can also use the next() function to manually iterate through the custom iterator
my_numbers = MyNumbers()
my_iter = iter(my_numbers)
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
print(next(my_iter))  # Output: 4
print(next(my_iter))  # Output: 5

