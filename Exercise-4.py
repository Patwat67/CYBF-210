# Exercise 4

class Stack:
    # Inits the stack as a private empty list
    def __init__(self):
        self._stack = []

    # Pushes onto stack by appending from the right
    def push(self, value):
        self._stack.append(value)

    # Pops from stack by popping from the right
    def pop(self):
        return self._stack.pop()

    # Returns true if the stack has any values, false if not
    def is_empty(self):
        if not self._stack:
            return True
        else:
            return False

class StringReverse:
    # Inits a private stack object and takes in a string
    def __init__(self, string:str):
        self.string = string
        self._stack = Stack()

    # Returns the reversed string
    def reverse_string(self):
        result = []
        if not self._stack.is_empty():
            raise Exception("Stack is not empty")

        # Pushes chars from the string into the stack
        for char in self.string:
            self._stack.push(char)

        # Pops chars back out and appends them to result list
        while not self._stack.is_empty():
            result.append(self._stack.pop())

        # Turns result list back into a string and returns it
        return ''.join(result)

# Entrypoint
if __name__ == "__main__":
    try:
        # Input string
        test_string = "Wow this is a cool string"
        # StringReverse object
        test = StringReverse(test_string)
        # Calls reverse_string method
        reversed_string = test.reverse_string()
        # Prints out result
        print(f"Original string: {test.string}\n"
              f"Reversed string: {reversed_string}")
    except KeyboardInterrupt:
        exit(1)