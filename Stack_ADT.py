class Stack:
    def __init__(self):
        self._stack = []

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        return self._stack.pop()

    def is_empty(self):
        if not self._stack:
            return True
        else:
            return False

class StringReverse:
    def __init__(self, string:str):
        self.string = string
        self._stack = Stack()

    def reverse_string(self):
        result = []
        if not self._stack.is_empty():
            raise Exception("Stack is not empty")

        for char in self.string:
            self._stack.push(char)

        while not self._stack.is_empty():
            result.append(self._stack.pop())

        return ''.join(result)

if __name__ == "__main__":
    try:
        test_string = "Wow this is a cool string"
        test = StringReverse(test_string)
        reversed_string = test.reverse_string()
        print(f"Original string: {test.string}\n"
              f"Reversed string: {reversed_string}")
    except KeyboardInterrupt:
        exit(1)