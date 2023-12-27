# Name: Frank Hodges
# OSU Email: hodgesf@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2 - Bag ADT and Dynamic Array
# Due Date: October 30th
# Description: This assignment consists of 2 parts.
# In the first part, there is an implementation of a Dynamic Array.
# Then in the second part, there is an implementation of a Bag ADT using the Dynamic Array from Part 1.

from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        This method changes the underlying storage capacity for the elements in the dynamic array.
        It does not change the values or the order of any elements currently stored in the array.

        :param new_capacity: the new size of the dynamic array
        :return: None
        """
        if new_capacity <= 0 or new_capacity < self._size:
            # Check if the new capacity is valid and larger than the current size
            return

        # Create a temporary array to hold the current elements
        temp = self._data

        # Create a new StaticArray with the specified new capacity
        self._data = StaticArray(new_capacity)

        # Copy elements from the temporary array to the new array
        for data in range(0, self._size):
            self._data[data] = temp[data]

        # Update the capacity to the new capacity
        self._capacity = new_capacity

    def append(self, value: object) -> None:
        """
        This method adds a new value at the end of the dynamic array.

        :param value: value to be added to the array
        :return: None
        """
        if self._size == self._capacity:
            # Check if the array is full (reached its current capacity)
            new_size = self._capacity * 2
            self.resize(new_size)

        # Add the value at the end of the array and increment the size
        self._data[self._size] = value
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method adds a new value at the specified index in the dynamic array.

        :param index: index where the new value needs to be added
        :param value: value to be added at the specified index
        :return: None
        """
        if index < 0 or index > self._size:
            # Check if the specified index is valid
            raise DynamicArrayException()

        if self._size == self._capacity:
            # Check if the dynamic array is full and needs to be resized
            self.resize(self._capacity * 2)

        for nums in range(self._size, index, -1):
            # Shift elements to make space for the new value
            self._data[nums] = self._data[nums - 1]

        # Insert the new value at the specified index
        self._data[index] = value

        # Increase the size of the dynamic array
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """
        This method removes the element at the specified index in the dynamic array.

        :param index: index of the value to be removed
        :return: None
        """
        if index < 0 or index > self._size - 1:
            # Check if the specified index is valid
            raise DynamicArrayException

        if self._size < (self._capacity / 4) and self._capacity > 10:
            # Check if the array is less than 1/4 full and the capacity is greater than 10
            # Calculate the new capacity, which is the maximum of doubling the size or 10
            new_capacity = max(self._size * 2, 10)
            self.resize(new_capacity)

        for nums in range(index, self._size - 1):
            # Shift elements to fill the gap created by removing the specified value
            self._data[nums] = self._data[nums + 1]

        # Set the last element to None and decrease the size of the array
        self._data[self._size - 1] = None
        self._size -= 1

    def pop_last_value(self):
        if self.is_empty():
            raise DynamicArrayException("Array is empty")

        last_val = self._data[self._size - 1]  # Access the last value
        self.remove_at_index(self._size - 1)  # Remove the value at the last index
        return last_val


    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        This method returns a new DynamicArray object that contains the requested number of
        elements from the original array, starting with the element located at the requested start
        index.

        :param start_index: index in the current array that the new array should start at
        :param size: size of the new array
        :return: a new Dynamic Array object with the specified values
        """
        if start_index < 0 or start_index >= self._size or size < 0:
            # Check if the start index and size are valid
            raise DynamicArrayException

        if start_index + size > self._size:
            # Check if the requested slice goes beyond the end of the array
            raise DynamicArrayException

        sliced_array = DynamicArray()  # Create a new DynamicArray to hold the sliced elements

        for items in range(start_index, start_index + size):
            # Copy elements from the original array to the sliced array
            sliced_array.append(self._data[items])

        return sliced_array

    def merge(self, second_da: "DynamicArray") -> None:
        """
        This method takes another DynamicArray object as a parameter, and appends all elements
        from this array onto the current one, in the same order in which they are stored in the input
        array.

        :param second_da: dynamic array to be merged with current array
        :return: None
        """
        for items in range(second_da._size):
            self.append(second_da._data[items])

    def map(self, map_func) -> "DynamicArray":
        """
        This method creates a new dynamic array where the value of each element is derived by
        applying a given map_func to the corresponding value from the original array.

        :param map_func: math f(x) to apply to each index
        :return: dynamic array
        """
        new_arr = DynamicArray()
        for items in range(0, self._size):
            temp_item = map_func(self._data[items])
            new_arr.append(temp_item)
        return new_arr

    def filter(self, filter_func) -> "DynamicArray":
        """
        This method creates a new dynamic array populated only with those elements from the
        original array for which filter_func returns True.

        :param filter_func: parameter to evaluate values in dynamic array as either true or false
        :return: dynamic array object that is filtered as specified by filter_func
        """
        new_arr = DynamicArray()
        for items in range(0, self._size):
            temp_item = filter_func(self._data[items])
            if temp_item is True:
                new_arr.append(self._data[items])
        return new_arr

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        This method sequentially applies the reduce_func to all elements of the dynamic array and
        returns the resulting value.

        :param reduce_func: value to reduce index by
        :param initializer:
        :return: object
        """
        ans = initializer
        for num in range(self._size):
            if ans is None:
                ans = self._data[num]
            else:
                ans = reduce_func(ans, self._data[num])
        return ans

def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    """
    receives a dynamic array
    already in sorted order, either non-descending or non-ascending. The function will return a
    tuple containing (in this order) a dynamic array comprising the mode (most-occurring)
    value/s of the array, and an integer that represents the highest frequency (how many times
    they appear).

    :param arr: array to find mode of
    :return: tuple containing the mode and frequency of the mode
    """
    if not arr:
        return DynamicArray(), 0  # Handle the case of an empty array

    mode = DynamicArray()
    mode.append(arr[0])
    max_frequency = 1
    current_frequency = 1
    arr_size = DynamicArray.length(arr)

    for items in range(1, arr_size):
        if arr[items] == arr[items - 1]:
            current_frequency += 1
        else:
            current_frequency = 1

        if current_frequency > max_frequency:
            max_frequency = current_frequency
            mode = DynamicArray()
            mode.append(arr[items])
        elif current_frequency == max_frequency:
            mode.append(arr[items])

    return mode, max_frequency


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
