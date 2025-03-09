# palindrome: string that reads the same forard and backward, example radar, toot, madam

# construct an algorithm to input a string of characters and check whether it is a palindrome

#first we can add each character of our string to the rear of the deque (at this point, the deque is acting like a regular queue).

#the deques front(end of list) will hold the strings first character. the deques rear (position 0 of list) will hold the last character of string. now we can use the dual functionality of deque to compare the first and last characters.

from Deque_implement import Deque


def pal_checker(a_string):
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_rear(ch)

    while char_deque.size() > 1:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            return False

    return True

print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))