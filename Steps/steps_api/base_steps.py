import random
import re

email_regex = re.compile(
    r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
)
def generate_unique_email(base_email, min_length=10, max_length=20):

    local_part, domain = base_email.split('@')
    special_chars = "._%+-"

    while True:
        modified_local_part = list(local_part)

        for _ in range(random.randint(1, 3)):
            pos = random.randint(0, len(modified_local_part))
            char = random.choice(special_chars)
            modified_local_part.insert(pos, char)

        if min_length < max_length:
            modified_length = random.randint(min_length, max_length)
        else:
            modified_length = max_length

        if len(modified_local_part) > modified_length:
            modified_local_part = modified_local_part[:modified_length]

        modified_local_part = ''.join(modified_local_part)
        email = f"{modified_local_part}@{domain}"

        if email_regex.match(email):
            return email

