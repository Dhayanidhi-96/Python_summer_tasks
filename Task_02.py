import string

def is_palindrome(text):
    text = text.lower()
    text = ''.join(char for char in text if char not in string.punctuation)
    text = text.replace(" ","")

    rev_text = text[::-1]

    return text == rev_text
def main():
    print("🌀 Palindrome Checker 🌀")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter a word or sentence :")

        if user_input.lower() == "exit":
            print("Goodbye...")
            break

        if is_palindrome(user_input):
            print("✅ It's a palindrome!\n")
        else:
            print("❌ Not a palindrome.\n")

if __name__ == "__main__":
    main()