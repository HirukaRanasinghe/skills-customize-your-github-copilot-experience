def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b

def is_palindrome(s: str) -> bool:
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]
