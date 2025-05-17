import requests
import hashlib


def password_leaks_count(hash_prefix, hash_suffix):
    # Send a request to the API with the first 5 characters of the hash - hash_prefix
    url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}")

    # Split response into lines, each line-> suffix:count
    hashes = (line.split(':') for line in res.text.splitlines())

    # Look for suffix that matches our hash suffix
    for h, count in hashes:
        if h == hash_suffix:
            return int(count)  # Return how many times it was leaked

    return 0  # Not found


def check_password(password):
    # Compute SHA1 hash of password by the format
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # Split the hash into prefix (first 5 chars) and suffix (rest)
    prefix, suffix = sha1pwd[:5], sha1pwd[5:]

    # Check how many times the password appeared in breaches
    count = password_leaks_count(prefix, suffix)
    return count


def main():
    password = input("Enter a password to check: ")
    count = check_password(password)
    if count:
        print(f"This password was found {count} times in data breaches. Consider changing it.")
    else:
        print("✅ This password was NOT found. Good job!")


if __name__ == '__main__':
    main()
