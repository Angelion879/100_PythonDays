import re


def password_validator(user_password):
    password_expected_pattern = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")

    return 'Accepted' if password_expected_pattern.fullmatch(user_password) else 'Unaccepted'
