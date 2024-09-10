import re


def password_validator(user_password):
    password_expected_pattern = re.compile(r"^.{8,}$")

    return 'Accepted' if password_expected_pattern.search(user_password) else 'Unaccepted'
