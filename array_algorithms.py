import sys
from list_creation import unordered_array


class InvalidLimitError(Exception):
    pass


class ArrayOverflowError(Exception):
    pass


class ArrayIndexOutOfRangeError(Exception):
    pass


class ArrayValueNotFoundError(Exception):
    pass


class ArrayValueDeletionError(Exception):
    pass


class Array:
    def __init__(self):
        self.array = unordered_array(len_array)
        self.limit = limit
        self.length = len(self.array)

    def insert_end(self, value):

        if self.length == self.limit:
            print("")
            raise ArrayOverflowError("Array Overflow")
        else:
            self.array.append(value)
            print(self.array)

    def insert_front(self, value):
        if self.length == self.limit:
            raise ArrayOverflowError("Array Overflow")
        else:
            i = 1
            while i > self.length:
                self.array[i] = self.array[i - 1]
                i = +1
            self.array[0] = value
            print(self.array)

    def insert_local(self, index, value):
        if self.length == self.limit:
            raise ArrayOverflowError("Array Overflow")
        elif index > self.length - 1:
            raise ArrayIndexOutOfRangeError("Array Index Out of Range")
        else:
            i = index
            while i < index:
                self.array[i] = self.array[i + 1]
                i = -1
            self.array[index] = value
            print(self.array)

    def insert_after_given_value(self, search, value):

        if self.length == self.limit:
            raise ArrayOverflowError("Array Overflow")
        else:
            i = 0
            while i < self.length:
                if self.array[i] == search:
                    break
                else:
                    i = +1
                if i == self.length:
                    print("no search value found no insertion")
                else:
                    j = self.length - 1
                    while j > i:
                        self.array[j + 1] = self.array[j]
                        j = j - 1
                        self.array[i + 1] = value
                        self.length = +1
        print(self.array)

    def remove_end(self):
        if self.length == 0:
            raise ArrayValueDeletionError("Deletion not possible no elements found")
        else:
            self.array.remove(self.length)
            print(self.array)

    def remove_front(self):
        if self.length == 0:
            raise ArrayValueDeletionError("Deletion not possible no elements found")
        else:
            self.array.remove(self.array[0])
            print(self.array)

    def remove_at_index(self, index):

        if self.length == 0:
            raise ArrayValueDeletionError("Deletion not possible no elements found")
        elif index > self.length - 1:
            raise ArrayIndexOutOfRangeError("Array Index Out of Range")
        else:
            self.array.remove(self.array[index])
        print(self.array)


if __name__ == '__main__':
    len_array = int(input("No of elements in the array: "))
    limit = int(input("Limit of the array: "))
    if len_array >= limit:
        raise InvalidLimitError("Limit must be grater than length of the array")

    a = Array()
    print(f"Array to be operated on: {a.array}")
    run_again = "y"
    while run_again == "y":
        operation_type = input("For insertion press (i)\n"
                               "For deletion press (d)\n"
                               "Enter your response with given string in brackets: ")
        if operation_type == "i":
            operation = input("(1)Insert at end: \n"
                              "(2)Insert at front: \n"
                              "(3)Insert at given index: \n"
                              "(4)insert after a given value: \n"
                              "Enter your response with given number in brackets: ")
            val = int(input("Enter the value to insert: "))
            if operation == "1":
                a.insert_end(val)
            elif operation == "2":
                a.insert_front(val)
            elif operation == "3":
                ind = int(input("Index for appending value: "))
                if ind > len_array:
                    raise ArrayIndexOutOfRangeError
                a.insert_local(val, ind)
            elif operation == "4":
                ind = int(input("After which value to append: "))
                if ind not in a.array:
                    raise ArrayValueNotFoundError
                a.insert_after_given_value(ind, val)
        elif operation_type == "d":
            operation = input("(5)delete at end: \n"
                              "(6)delete at front: \n"
                              "(7)Delete at given index: \n"
                              "Enter your response with given number in brackets: ")
            if operation == "5":
                a.remove_end()
            elif operation == "6":
                a.remove_front()
            elif operation == "7":
                ind = int(input("Index to delete the element: "))
                a.remove_at_index(ind)
        run_again = input("Want to run program again - (y)Yes or (n)No: ")
    if run_again == "n":
        sys.exit("Exit operation commanded")
