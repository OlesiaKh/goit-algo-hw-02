from collections import deque

def is_palindrome(s) -> bool:
    prep = ''.join([ch.lower() for ch in s if ch.isalpha()])

    deq = deque(prep)

    while len(deq) > 1:
        if deq.pop() != deq.popleft():
            return False
    return True

print(is_palindrome("Pan ap"))


# Тестування функції
assert is_palindrome("A man, a plan, a canal, Panama") is True, "Провалено: 'A man, a plan, a canal, Panama'"
assert is_palindrome("Hello") is False, "Провалено: 'Hello'"

# Паліндроми
assert is_palindrome("Racecar") is True, "Провалено: 'Racecar'"
assert is_palindrome("Able was I ere I saw Elba") is True, "Провалено: 'Able was I ere I saw Elba'"
assert is_palindrome("Madam In Eden, I’m Adam") is True, "Провалено: 'Madam In Eden, I’m Adam'"
assert is_palindrome("A Santa at NASA") is True, "Провалено: 'A Santa at NASA'"

# Не паліндроми
assert is_palindrome("Python") is False, "Провалено: 'Python'"
assert is_palindrome("OpenAI") is False, "Провалено: 'OpenAI'"

# Зі знаками пунктуації та пробілами
assert is_palindrome("Was it a car or a cat I saw?") is True, "Провалено: 'Was it a car or a cat I saw?'"
assert is_palindrome("No 'x' in Nixon") is True, "Провалено: 'No 'x' in Nixon'"