from deque import Deque

def is_palindrome(word):
    deq = Deque()
    for ch in word:
        deq.add_rear(ch)
    #deq.items = word.split()

    while not deq.is_empty():
        if (deq.peek_front() != deq.peek_rear()):
            return False

        if not deq.is_empty():
            deq.remove_front()

        if deq.remove_front():
            deq.remove_rear()
    return True

def test_is_palindrome():
    inp = input("Enter a string to test for Palindrome: ")
    print(is_palindrome(inp))

if __name__ == "__main__":
    test_is_palindrome()