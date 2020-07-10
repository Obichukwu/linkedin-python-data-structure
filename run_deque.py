from deque import Deque

def is_palindrome(word):
    deq = Deque()
    for ch in word:
        deq.add_rear(ch)
    #deq.items = word.split()

    while deq.size() >= 2:
        front = deq.remove_front()
        rear = deq.remove_rear()

        if (front != rear):
            return False

    return True

def test_is_palindrome():
    inp = input("Enter a string to test for Palindrome: ")
    print(is_palindrome(inp))

if __name__ == "__main__":
    test_is_palindrome()