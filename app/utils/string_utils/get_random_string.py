import string
import random

def get_random_string(min_length, max_length):
    """
    Return a random string with a random length where min_length <= length <= max_length
    @param min_length Integer minimum length
    @param max_length Integer maximum length
    """
    try:
        length = random.randint(min_length, max_length)
        choices = string.ascii_lowercase + string.digits
        return "".join(random.choice(choices) for i in range(length))
    except Exception:
        return False